console.log("dashboard loaded ")

let allProblems = []
let showAllProblems = false

/* =========================
   TOKEN
========================= */

const token = localStorage.getItem("token")

if(!token){

    window.location.href = "index.html"

}

/* =========================
   PROFILE
========================= */

async function loadProfile(){

    try{

        const response = await fetch(

            "http://127.0.0.1:8000/leetcode/profile",

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        const data = await response.json()

        document.getElementById("profileCard").innerHTML = `

        <div class="stat-card easy">
            <h3>Easy</h3>
            <p>${data.easy_solved}</p>
        </div>

        <div class="stat-card medium">
            <h3>Medium</h3>
            <p>${data.medium_solved}</p>
        </div>

        <div class="stat-card hard">
            <h3>Hard</h3>
            <p>${data.hard_solved}</p>
        </div>

        <div class="stat-card">
            <h3>Total</h3>
            <p>${data.total_solved}</p>
        </div>

        <div class="stat-card">
            <h3>Ranking</h3>
            <p>${data.ranking}</p>
        </div>

        <div class="stat-card">
            <h3>Contest</h3>
            <p>${data.contest_rating}</p>
        </div>

        `

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   SYNC
========================= */

document.getElementById("syncBtn")
.addEventListener(
"click",
async()=>{

    try{

        const response = await fetch(

            "http://127.0.0.1:8000/leetcode/sync",

            {

                method:"POST",

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        const data = await response.json()

        alert(data.message)

        loadProfile()

    }

    catch(error){

        console.log(error)

    }

})

/* =========================
   ADD PROBLEM
========================= */

document.getElementById("problemForm")
.addEventListener(
"submit",
async(e)=>{

    e.preventDefault()

    const payload = {

        title:document.getElementById("title").value,

        difficulty:document.getElementById("difficulty").value,

        topic:document.getElementById("topic").value,

        time_spend:parseInt(
            document.getElementById("time_spend").value
        ),

        notes:document.getElementById("notes").value

    }

    try{

        await fetch(

            "http://127.0.0.1:8000/problems/add",

            {

                method:"POST",

                headers:{

                    "Content-Type":"application/json",

                    Authorization:`Bearer ${token}`

                },

                body:JSON.stringify(payload)

            }

        )

        alert("Problem Added ")

        document.getElementById("problemForm").reset()

        loadProblems()
        loadStreak()
        loadHeatmap()

    }

    catch(error){

        console.log(error)

    }

})

/* =========================
   LOAD PROBLEMS
========================= */

async function loadProblems(){

    try{

        const response = await fetch(

            "http://127.0.0.1:8000/problems/my-problem",

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        allProblems = await response.json()

        renderProblems()

        loadCharts(allProblems)

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   RENDER PROBLEMS
========================= */

function renderProblems(){

    const tableBody =
    document.getElementById("problemTableBody")

    const toggleBtn =
    document.getElementById("toggleProblemsBtn")

    tableBody.innerHTML = ""

    let visibleProblems = []

    if(showAllProblems){

        visibleProblems = allProblems

    }

    else{

        visibleProblems =
        allProblems.slice(0,6)

    }

    visibleProblems.forEach(problem=>{

        tableBody.innerHTML += `

        <tr>

            <td>${problem.title}</td>

            <td>${problem.difficulty}</td>

            <td>${problem.topic}</td>

            <td>${problem.time_spend} min</td>

            <td>

                <button onclick="deleteProblem(${problem.id})">
                    Delete
                </button>

            </td>

        </tr>

        `

    })

    if(allProblems.length > 6){

        toggleBtn.style.display = "block"

        toggleBtn.innerText =
        showAllProblems
        ? "Show Less "
        : "Show More "

    }

    else{

        toggleBtn.style.display = "none"

    }

}

/* =========================
   TOGGLE BUTTON
========================= */

document.getElementById("toggleProblemsBtn")
.addEventListener(
"click",
()=>{

    showAllProblems =
    !showAllProblems

    renderProblems()

})

/* =========================
   DELETE
========================= */

async function deleteProblem(id){

    try{

        await fetch(

            `http://127.0.0.1:8000/problems/${id}`,

            {

                method:"DELETE",

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        loadProblems()
        loadStreak()
        loadHeatmap()

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   CHARTS
========================= */

let difficultyChart
let topicChart

function loadCharts(problems){

    const difficultyCount = {

        Easy:0,
        Medium:0,
        Hard:0

    }

    const topicCount = {}

    problems.forEach(problem=>{

        difficultyCount[
            problem.difficulty
        ]++

        if(topicCount[problem.topic]){

            topicCount[
                problem.topic
            ]++

        }

        else{

            topicCount[
                problem.topic
            ] = 1

        }

    })

    const diffCtx =
    document.getElementById("difficultyChart")

    if(difficultyChart){

        difficultyChart.destroy()

    }

    difficultyChart =
    new Chart(diffCtx,{

        type:"doughnut",

        data:{

            labels:[
                "Easy",
                "Medium",
                "Hard"
            ],

            datasets:[{

                data:[

                    difficultyCount.Easy,
                    difficultyCount.Medium,
                    difficultyCount.Hard

                ],

                backgroundColor:[

                    "#22C55E",
                    "#F59E0B",
                    "#EF4444"

                ]

            }]

        }

    })

    const topicCtx =
    document.getElementById("topicChart")

    if(topicChart){

        topicChart.destroy()

    }

    topicChart =
    new Chart(topicCtx,{

        type:"bar",

        data:{

            labels:Object.keys(topicCount),

            datasets:[{

                label:"Problems",

                data:Object.values(topicCount),

                backgroundColor:"#38BDF8"

            }]

        }

    })

}

/* =========================
   STREAK
========================= */

async function loadStreak(){

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/streak/all",

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        const data =
        await response.json()

        document.getElementById("streakCard").innerHTML = `

        <div class="stat-card">
            <h3> Current</h3>
            <p>${data.current_streak}</p>
        </div>

        <div class="stat-card">
            <h3> Longest</h3>
            <p>${data.longest_streak}</p>
        </div>

        <div class="stat-card">
            <h3> Active Days</h3>
            <p>${data.active_days}</p>
        </div>

        <div class="stat-card">
            <h3> Consistency</h3>
            <p>${data.consistency_percentage}%</p>
        </div>

        `

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   HEATMAP
========================= */

async function loadHeatmap(){

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/streak/heatmap",

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        const data =
        await response.json()

        const container =
        document.getElementById("heatmapContainer")

        container.innerHTML = ""

        data.forEach(day=>{

            let level = "level-1"

            if(day.count >= 2){

                level = "level-2"

            }

            if(day.count >= 4){

                level = "level-3"

            }

            if(day.count >= 6){

                level = "level-4"

            }

            container.innerHTML += `

            <div
                class="heatmap-box ${level}"
                title="${day.date} : ${day.count} problems"
            ></div>

            `

        })

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   AI
========================= */

document.getElementById("loadRecommendation")
.addEventListener(
"click",
async()=>{

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/dashboard/ai-recommendation",

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        const data =
        await response.json()

        let html = ""

        data.message.forEach(msg=>{

            html += `<p>🚀 ${msg}</p>`

        })

        document.getElementById("result").innerHTML = html

    }

    catch(error){

        console.log(error)

    }

})

/* =========================
   LOGOUT
========================= */

document.getElementById("logoutBtn")
.addEventListener(
"click",
()=>{

    localStorage.removeItem("token")

    window.location.href = "index.html"

})

/* =========================
   INITIAL LOAD
========================= */

loadProfile()
loadProblems()
loadStreak()
loadHeatmap()