class ITax {
    calculate() {
        throw new Error("Method 'calculate' not implemented")
    }

    print() {
        throw new Error("Method 'print' not implemented")
    }
}

class Invoice {
    constructor(client, items) {
        this.client = client;
        this.items = items;
    }

    calculateTotal() {
        let total = 0;
        this.items.forEach(item => {
            total += item.price * item.quantity;
        });
        return total;
    }

    print() {
        console.log(`Invoice: ${this.client}`);
        this.items.forEach(item => {
            console.log(`${item.name} - Quantity: ${item.quantity}, Unit Price: ${item.price}`);
        });
        console.log(`Total: ${this.calculateTotal()}`);
    }

    calculateWithTax(invoiceType) {
        const inv = new invoiceType(this)

        inv.print()
    }
}

class IVA extends ITax {
    taxRate = 0.19
    constructor(invoice) {
        super()
        this.invoice = invoice
    }

    calculate() {
        return this.invoice.calculateTotal() * (1 + this.taxRate)
    }

    print() {
        this.invoice.print()
        console.log("IVA Tax: " + this.calculate())
    }
}

class ICO extends ITax {
    taxRate = 0.556
    constructor(invoice) {
        super()
        this.invoice = invoice
    }

    calculate() {
        return this.invoice.calculateTotal() * (1 + this.taxRate)
    }

    print() {
        this.invoice.print()
        console.log("ICO Tax: " + this.calculate())
    }
}

// Ejemplo de uso
const items = [
    { name: 'Producto 1', quantity: 2, price: 10 },
    { name: 'Producto 2', quantity: 1, price: 20 }
];

const invoice = new Invoice('client 1', items);
invoice.calculateWithTax(IVA)