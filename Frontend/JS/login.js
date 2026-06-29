
console.log("login.js loaded 😎🔥")

const loginForm =
document.getElementById(
    "loginForm"
)

loginForm.addEventListener(
"submit",
async (e)=>{

    e.preventDefault()

    const username =
    document.getElementById(
        "username"
    ).value

    const password =
    document.getElementById(
        "password"
    ).value

    const formData =
    new URLSearchParams()

    formData.append(
        "username",
        username
    )

    formData.append(
        "password",
        password
    )

    try{

        const response =
        await fetch(

            "http://127.0.0.1:8000/auth/login",

            {

                method:"POST",

                headers:{

                    "Content-Type":
                    "application/x-www-form-urlencoded"

                },

                body:
                formData

            }

        )

        const data =
        await response.json()

        console.log(
            "LOGIN RESPONSE 😎🔥",
            data
        )

        if(response.ok){

            localStorage.setItem(

                "token",

                data.access_token

            )

            console.log(

                "TOKEN SAVED 😎🔥",

                localStorage.getItem(
                    "token"
                )

            )

            alert(
                "Login successful 😎🔥"
            )

            window.location.href =
            "dashboard.html"

        }

        else{

            alert(

                data.detail ||
                data.Message ||
                "Login failed 😭🔥"

            )

        }

    }

    catch(error){

        console.log(error)

        alert(
            "Server error 😭🔥"
        )

    }

})

