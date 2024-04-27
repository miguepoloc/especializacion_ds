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
        switch (invoiceType) {
            case "iva":
                return this.calculateTotal() * (1 + 0.19)
            case "ico":
                return this.calculateTotal() * (1 + 0.08)
            default:
                return this.calculateTotal()
        }
    }
}

const invoice = new Invoice("0220", [
    { name: 'Producto 1', quantity: 2, price: 10 },
    { name: 'Producto 2', quantity: 1, price: 20 }
])

invoice.print()
console.log(`Total: ${invoice.calculateWithTax("iva")}`)