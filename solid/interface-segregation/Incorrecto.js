class Invoice {
  client = "";
  seller = "";
  items = [];

  constructor(client, seller, items, type = "invoice") {
    this.number = Math.round(Math.random() * 200);
    this.client = client;
    this.seller = seller;
    this.items = items;
    this.type = type;
  }

  getTotal() {
    return this.items.reduce(
        (acc, curr) => acc + curr.quantity * curr.price,
        0
      );
  }

  calculateTotal() {
    const value = this.getTotal()
    if (this.type === "bill") {
      return this.applyVATTax(value);
    }

    return value;
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

const invoice = new Invoice("Juan", "Pedro", items, "invoice");

invoice.print();
