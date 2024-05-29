document.addEventListener("DOMContentLoaded", function () {
  const formulario = document.getElementById("formulario");
  const desempregadosDiv = document.getElementById("desempregados");

  // Função para carregar os desempregados
  function carregarDesempregados() {
    axios
      .get("/desempregados")
      .then(function (response) {
        const desempregados = response.data;
        desempregadosDiv.innerHTML = "";
        desempregados.forEach(function (desempregado) {
          const desempregadoDiv = document.createElement("div");
          desempregadoDiv.textContent = `Nome: ${desempregado[1]}, Idade: ${desempregado[2]}, Telefone: ${desempregado[3]}, Formação: ${desempregado[4]}, Email: ${desempregado[5]}`;
          desempregadosDiv.appendChild(desempregadoDiv);
        });
      })
      .catch(function (error) {
        console.error("Erro ao carregar os desempregados:", error);
      });
  }

  // Evento de envio do formulário
  formulario.addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = new FormData(formulario);
    axios
      .post("/adicionar_desempregado", formData)
      .then(function (response) {
        console.log(response.data);
        carregarDesempregados();
      })
      .catch(function (error) {
        console.error("Erro ao adicionar desempregado:", error);
      });
  });

  // Carregar os desempregados quando a página é carregada
  carregarDesempregados();
});
