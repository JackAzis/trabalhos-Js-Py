let vitorias = 106
let derrotas = 5

function subtracao() {
    return vitorias - derrotas;  
}

let saldoVitorias = subtracao()
if (saldoVitorias <=10){
    nivel = "Ferro"
}
else if ((saldoVitorias >= 11) && (saldoVitorias <= 20)){
    nivel = "Bronze"
}
else if ((saldoVitorias >= 21) && (saldoVitorias <= 50)){
    nivel = "Prata"
}
else if ((saldoVitorias >= 51) && (saldoVitorias <= 80)){
    nivel = "Ouro"
}
else if ((saldoVitorias >= 81) && (saldoVitorias <= 90)){
    nivel = "Diamante"
}
else if ((saldoVitorias >= 91) && (saldoVitorias <= 100)){
    nivel = "Lendario"
}
else if (saldoVitorias >= 101) {
    nivel = "Imortal"
}
console.log("O Herói tem de saldo de " + saldoVitorias + " está no nivel " + nivel)
