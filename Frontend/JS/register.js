const registerForm =
document.getElementById(
    "registerForm"
)
registerForm.addEventListener(
    "submit",
    async (e)=>{
        e.preventDefault()
        const payload={
            username:
            document.getElementById(
                "username"
            ).value,
            email:
            document.getElementById(
                "email"
            ).value,
            password:
            document.getElementById(
                "password"
            ).value,
            leetcode_username:
            document.getElementById(
                "leetcode_username"
            ).value,
            bio:
            document.getElementById(
                "bio"
            ).value
        }
        try{
            const responce=await apiRequest(
                "/auth/register","POST",payload
            )
            console.log(responce)
            if (
                responce.status === 200|| responce.status === 201
            ){
                alert(
                    "Registration Successful"
                )
                window.location.href="login.html"

            }
            else{
                alert(
                    responce.data.detail||
                    "Registration failed"
                )
            }
        }
        catch(error){
            console.log(error)
            alert("Server error")
        }
    }
)