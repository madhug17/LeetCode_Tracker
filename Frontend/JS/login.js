
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

        try{

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

                // SAVE TOKEN 😎🔥
                localStorage.setItem(
                    "token",
                    data.access_token
                )
                console.log(
                    "Token_saved",
                    data.access_token
                )

                localStorage.setItem(
                    "refresh_token",
                    data.refresh_token
                )

                console.log(
                    "TOKEN SAVED 😎🔥",
                    data.access_token
                )

                alert(
                    "Login Success 😎🔥"
                )

                window.location.href =
                "dashboard.html"

            }

            else{

                alert(
                    data.detail ||
                    data.Message ||
                    "Login Failed 😭🔥"
                )

            }

        }

        catch(error){

            console.log(error)

            alert(
                "Server Error 😭🔥"
            )

        }

    }
)

