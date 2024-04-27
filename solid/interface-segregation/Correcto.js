class Invoice {
  constructor(client, seller, items) {
    this.number = Math.round(Math.random() * 200);
    this.client = client;
    this.seller = seller;
    this.items = items;
  }

  print() {
    throw new Error("Method 'print' not implemented");
  }

  getTotal() {
    throw new Error("Method 'getTotal' not implemented");
  }

  calculateTotal() {
    throw new Error("Method 'calculateTotal' not implemented");
  }
}

class PurchaseInvoice extends Invoice {
  taxRate = 0.19;
  constructor(number, client, seller, items) {
    super(number, client, seller, items);
  }

  getTotal() {
    return this.items.reduce(
      (acc, curr) => acc + curr.quantity * curr.price,
      0
    );
  }

  calculateTotal() {
    return this.applyVATTax(this.getTotal());
  }

  applyVATTax(total) {
    return total * (1 + 0.19);
  }

  print() {
    console.log("===| Printing Invoice |===");
    console.log("Number: ", this.number);
    console.log("Seller: ", this.seller);
    console.log("Client: ", this.client);
    console.log("Total: ", this.calculateTotal());
  }
}

class SalesInvoice extends Invoice {
  constructor(number, client, seller, items) {
    super(number, client, seller, items);
  }

  getTotal() {
    return this.items.reduce(
      (acc, curr) => acc + curr.quantity * curr.price,
      0
    );
  }

  calculateTotal() {
    return this.getTotal();
  }

  applyVATTax(total) {
    return total * (1 + 0.19);
  }

  print() {
    console.log("===| Printing Invoice |===");
    console.log("Number: ", this.number);
    console.log("Seller: ", this.seller);
    console.log("Client: ", this.client);
    console.log("Total: ", this.calculateTotal());
  }
}

const items = [
  { product: "Item 1", quantity: 3, price: 2500 },
  { product: "Item 2", quantity: 4, price: 1500 },
  { product: "Item 3", quantity: 10, price: 4333 },
];

const invoice = new SalesInvoice("Juan", "Pedro", items);
invoice.print();
