function obterNomeDiaSemana(data) {
            const nomesDiasSemana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"];
            return nomesDiasSemana[data.getDay()];
        }

        function atribuirFuncaoAleatoria() {
            const funcoes = ["Kiosk", "Check-in", "Desembarque", "Loja"];
            return funcoes[Math.floor(Math.random() * funcoes.length)];
        }

        function gerarProgramacao() {
            const diaSelecionado = document.getElementById("dia").value;
            const mesSelecionado = document.getElementById("mes").value;
            const dataSelecionada = `${diaSelecionado}/${mesSelecionado}`;
            const tabelaContainer = document.getElementById("tabelaContainer");
            const dataSelecionadaElement = document.getElementById("dataSelecionada");

            if (!diaSelecionado || !mesSelecionado) {
                alert("Por favor, selecione um dia e um mês.");
                tabelaContainer.style.display = "none";
                return;
            }

            // Aqui você pode definir o número de funcionários que deseja exibir na tabela.
            const numeroFuncionarios = 5;

            const tabela = document.querySelector("table");
            const tabelaBody = tabela.querySelector("tbody");
            tabelaBody.innerHTML = "";

            for (let i = 0; i < numeroFuncionarios; i++) {
                const funcionario = `Funcionário ${i + 1}`;
                const funcao = atribuirFuncaoAleatoria();
                const row = tabelaBody.insertRow();
                row.insertCell(0).textContent = funcionario;
                row.insertCell(1).textContent = funcao;
            }

            dataSelecionadaElement.textContent = dataSelecionada;
            tabelaContainer.style.display = "block";
        }

        // Preencher opções de seleção para os dias e meses aqui...
        const diasSelect = document.getElementById("dia");
        const mesesSelect = document.getElementById("mes");

        for (let i = 1; i <= 31; i++) {
            const option = document.createElement("option");
            option.value = i;
            option.textContent = i;
            diasSelect.appendChild(option);
        }

        const nomesMeses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

        for (let i = 1; i <= 12; i++) {
            const option = document.createElement("option");
            option.value = i;
            option.textContent = nomesMeses[i - 1];
            mesesSelect.appendChild(option);
        }
