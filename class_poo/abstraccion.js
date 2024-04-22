class Bill {
  client;
  products = [];
  constructor(client) {
    this.client = client;
    this.date = new Date();
  }

  addProduct(name, price, quantity) {
    this.products.push({ name, price, quantity });
  }

  print() {
    console.log(
      `Factura de compra\nCliente: ${this.client}\nFecha: ${this.date}`
    );
    this.products.forEach((product) => {
      console.log(
        `\t${product.quantity} x ${product.name}: total: $${
          product.price * product.quantity
        }`
      );
    });
  }
}

class Invoice {
  client = "";
  seller = "";
  products = [];
  date = 0;
  numeration = 0;

  constructor(client, seller) {
    if (!client || !seller) throw Error("Cliente y vendedor son obligatorios");

    this.client = client;
    this.seller = seller;
    this.numeration = Math.floor(Math.random() * 1000) + 1; //
    this.date = new Date();
  }

  addProduct(name, price, quantity) {
    this.products.push({ name, price, quantity });
  }

  print() {
    console.log(
      `Factura de venta N°${this.numeration}\nCliente: ${this.client}\nFecha: ${this.date}`
    );
    this.products.forEach((product) => {
      console.log(
        `\t${product.quantity} x ${product.name}: total: $${
          product.price * product.quantity
        }`
      );
    });
  }
}

//

const fv = new Invoice("Juan", "Manuela");

fv.addProduct("Lechuga", 2500, 13);
fv.addProduct("Legos", 15000, 2);

fv.print();

console.log("=======================================================");

const bill = new Bill("Juan");

bill.addProduct("Lechuga", 2500, 13);
bill.addProduct("Legos", 15000, 2);

bill.print();
