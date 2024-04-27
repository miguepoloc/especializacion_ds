class NewInvoice {
    constructor(number, balance, amount, invoiceDate) {
        this.id = this.generateUniqueId();
        this.number = number;
        this.balance = balance;
        this.amount = amount;
        this.invoiceDate = invoiceDate;
    }

    generateUniqueId() {
        return Math.floor(Math.random() * 1000000000);
    }

    print() {
        console.log("Invoice #" + this.number);
        console.log("Amount: " + this.amount);
        console.log("Balance: " + this.balance);
        console.log("Invoice Date: " + this.invoiceDate);
    }
}

class TaxInvoice {
    taxRate = 0.21
    constructor(invoice) {
        this.invoice = invoice
    }

    calculateTax() {
        return this.invoice.amount * (1 + this.taxRate)
    }

    print() {
        this.invoice.print()
        console.log(`Tax Amount: ${this.calculateTax()}`)
    }
}

let inv = new NewInvoice('001', 2500, 5000, new Date())
const newInvoice = new TaxInvoice(inv)

console.log('\nNew Invoice')

newInvoice.print() // Invoice #001