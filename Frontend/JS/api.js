const BASE_URL = "https://leetcode-tracker-6nuw.onrender.com";
function getToken(){
    return localStorage.getItem('token')
}
async function apiRequest(
    endpoint,
    method="GET",
    body=null
) {
    const headers = {
        "Content-Type":
        "application/json"
    }
    const token = getToken()
    if (token){
        headers["Authorization"] = `Bearer ${token}`
    }
    const config = {
        method,
        headers
    }
    if (body){
        config.body=JSON.stringify(body)
    }
    const responce = await fetch(
        `${API_BASE}${endpoint}`,
        config
    )
    const data = 
    await responce.json()
    return{
        status:responce.status,
        data
    }
}