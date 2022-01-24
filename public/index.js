async function carregarAnimais(){
    const response = await axios.get("http://localhost:8000/animais")
    
    const animais = response.data

    const lista = document.getElementById("form-animais")

    lista.innerHTML = ""

    animais.forEach(animal => {
        const item = document.createElement("li")
        item.innerText = animal.nome
        const linha =`${animal.nome} - Idade: ${animal.idade} - Cor: ${animal.cor}`
        lista.appendChild(item)
    });
}

function adcionarDados(){
    const form_animal = document.getElementById("form-animais")
    const input_nome = document.getElementById("nome")

    form_animal.onsubmit = async(event) => {
        event.preventDefault()
        const nome_animal = input_nome.value
        await axios.post("http://localhost:8000/animais",{
            nome: nome_animal,
            idade:24,
            sexo:"macho",
            cor:"branco",
        })
        alert("Animal cadatrado")
    }
}

function app(){
    console.log("App iniciada")
    carregarAnimais()
    adcionarDados()
}

app()