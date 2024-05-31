async function addDesempregado() {
  const nome = document.getElementById("nome").value;
  const idade = document.getElementById("idade").value;
  const telefone = document.getElementById("telefone").value;
  const formacao = document.getElementById("formacao").value;
  const email = document.getElementById("email").value;

  const response = await fetch("/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ nome, idade, telefone, formacao, email }),
  });

  const result = await response.json();
  alert(result.success || result.error);

  // Limpa os campos do formulário após a adição bem-sucedida
  document.getElementById("nome").value = "";
  document.getElementById("idade").value = "";
  document.getElementById("telefone").value = "";
  document.getElementById("formacao").value = "";
  document.getElementById("email").value = "";
}
