<h1>Script para adicionar todos os servicos realizado pela empresa</h1>


<h4>Windows - Powershell</h4>
get-childItem -path ./file  -filter *.csv | foreach-object {
  python main.py "./file/$($_.name)" --service
}

<h4>Linux - Bash</h4>
