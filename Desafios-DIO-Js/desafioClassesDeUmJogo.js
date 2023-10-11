let invoice = {
	name: "Baki",
	age: 28,
	classes:{
    	0: ["Mago", "Magia"],
		1: ["Guerreiro", "Espada"],
        2: ["Monge", "Punho"],
        3: ["Ninja", "Shuriken"]
    }
}

generateInvoice (invoice)

function generateInvoice(invoice){
    
    for (let index in invoice.classes){
        let [tipo, ataque] = invoice.classes[index]
            console.log(`o ${tipo} atacou usando ${ataque}`)
    }    
}