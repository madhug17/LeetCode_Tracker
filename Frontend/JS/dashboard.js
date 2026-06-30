console.log("dashboard loaded 😎🔥")

/* =========================
   TOKEN 😎🔥
========================= */

const token =
localStorage.getItem(
    "token"
)

console.log(
    "TOKEN FROM STORAGE 😎🔥",
    token
)

if(!token){

    alert(
        "No token found 😭🔥"
    )

    window.location.href =
    "login.html"

}

/* =========================
   LOAD PROFILE 
========================= */

async function loadProfile(){

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/leetcode/profile",

            {

                method:"GET",

                headers:{

                    Authorization:
                    `Bearer ${token}`

                }

            }

        )

        console.log(
            "PROFILE RESPONSE ",
            response
        )

        if(response.status === 401){

            alert(
                "Session expired 😭🔥"
            )

            localStorage.removeItem(
                "token"
            )

            window.location.href =
            "login.html"

            return

        }

        const data =
        await response.json()

        console.log(data)

        document.getElementById(
            "profileCard"
        ).innerHTML = `

        <div class="stat-card easy">

            <h3>Easy 😎🔥</h3>

            <p>${data.easy_solved}</p>

        </div>

        <div class="stat-card medium">

            <h3>Medium 🚀</h3>

            <p>${data.medium_solved}</p>

        </div>

        <div class="stat-card hard">

            <h3>Hard 😭🔥</h3>

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

            <h3>Contest Rating</h3>

            <p>${data.contest_rating}</p>

        </div>

        `

    }

    catch(error){

        console.log(error)

        alert(
            "Profile loading failed 😭🔥"
        )

    }

}

/* =========================
   SYNC PROFILE 😎🔥
========================= */

document
.getElementById(
    "syncBtn"
)
.addEventListener(
"click",
async ()=>{

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/leetcode/sync",

            {

                method:"POST",

                headers:{

                    Authorization:
                    `Bearer ${token}`

                }

            }

        )

        console.log(
            "SYNC RESPONSE 😎🔥",
            response
        )

        const data =
        await response.json()

        console.log(data)

        alert(
            data.message
        )

        loadProfile()

    }

    catch(error){

        console.log(error)

        alert(
            "Sync failed 😭🔥"
        )

    }

})

/* =========================
   ADD PROBLEM 😎🔥
========================= */

document
.getElementById(
    "problemForm"
)
.addEventListener(
"submit",
async (e)=>{

    e.preventDefault()

    try{

        const payload = {

            title:
            document.getElementById(
                "title"
            ).value,

            difficulty:
            document.getElementById(
                "difficulty"
            ).value,

            topic:
            document.getElementById(
                "topic"
            ).value,

            time_spend:
            parseInt(
                document.getElementById(
                    "time_spend"
                ).value
            ),

            notes:
            document.getElementById(
                "notes"
            ).value

        }

        console.log(payload)

        const response =
        await fetch(

            "http://127.0.0.1:8000/problems/add",

            {

                method:"POST",

                headers:{

                    "Content-Type":
                    "application/json",

                    Authorization:
                    `Bearer ${token}`

                },

                body:
                JSON.stringify(payload)

            }

        )

        console.log(response)

        const data =
        await response.json()

        console.log(data)

        alert(
            "Problem Added 😎🔥"
        )

        document.getElementById(
            "problemForm"
        ).reset()

        loadProblems()

    }

    catch(error){

        console.log(error)

        alert(
            "Failed to add problem 😭🔥"
        )

    }

})

/* =========================
   LOAD PROBLEMS 😎🔥
========================= */

async function loadProblems(){

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/problems/my-problem",

            {

                method:"GET",

                headers:{

                    Authorization:
                    `Bearer ${token}`

                }

            }

        )

        console.log(response)

        const data =
        await response.json()

        console.log(
            "PROBLEMS 😎🔥",
            data
        )

        const table =
        document.getElementById(
            "problemTable"
        )

        table.innerHTML = ""

        data.forEach(problem => {

            table.innerHTML += `

            <tr>

                <td>${problem.title}</td>

                <td>${problem.difficulty}</td>

                <td>${problem.topic}</td>

                <td>${problem.time_spend}</td>

                <td>

                    <button
                    onclick="editProblem(${problem.id})"
                    >

                    Edit

                    </button>

                    <button
                    onclick="deleteProblem(${problem.id})"
                    >

                    Delete

                    </button>

                </td>

            </tr>

            `

        })

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   DELETE 😎🔥
========================= */

async function deleteProblem(id){

    try{

        await fetch(

            `http://127.0.0.1:8000/problems/${id}`,

            {

                method:"DELETE",

                headers:{

                    Authorization:
                    `Bearer ${token}`

                }

            }

        )

        loadProblems()

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   EDIT 😎🔥
========================= */

async function editProblem(id){

    const title =
    prompt(
        "Enter new title 😎🔥"
    )

    if(!title){

        return

    }

    try{

        await fetch(

            `http://127.0.0.1:8000/problems/${id}`,

            {

                method:"PUT",

                headers:{

                    "Content-Type":
                    "application/json",

                    Authorization:
                    `Bearer ${token}`

                },

                body:
                JSON.stringify({

                    title:title

                })

            }

        )

        loadProblems()

    }

    catch(error){

        console.log(error)

    }

}

/* =========================
   LOGOUT 😎🔥
========================= */

document
.getElementById(
    "logoutBtn"
)
.addEventListener(
"click",
()=>{

    localStorage.removeItem(
        "token"
    )

    window.location.href =
    "login.html"

})

/* =========================
   AUTO LOAD 😎🔥
========================= */

loadProfile()
loadProblems()

