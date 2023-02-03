async function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // console.log('cookie', cookie)
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


async function makeRequest(url, method) {
    let response = await fetch(url, method);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        // throw error;
        return response.json()
    }
}


async function buttonClick(event) {
    const csrftoken = await getCookie('csrftoken');
    let target = event.target;
    let url = target.dataset['link'];
    console.log(url)
    console.log(csrftoken)
    let id = target.dataset.id;
    let input1 = document.getElementById('input1').value;
    let input2 = document.getElementById('input2').value;
    let data = {
        "first_numbers": input1,
        "second_numbers": input2
    }
    let str_data = JSON.stringify(data)
    let response = await makeRequest(url, {
        method : "POST",
        headers : {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json"
        },
        body: str_data
    })
    console.log(response)
    let result = document.getElementById('result')
    // result.innerHTML = `Answer: ${response.result.answer}`
    // return response

    if (response.result.answer) {
        result.innerHTML = `Answer: ${response.result.answer}`;
        result.style.color = "green";
    } else {
        result.innerHTML = `Error: ${response.result.Error}`;
        result.style.color = 'red'
    }
    return response
}



