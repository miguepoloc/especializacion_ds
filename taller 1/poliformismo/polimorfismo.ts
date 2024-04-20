abstract class WatchP {
    brand: string;
    model: string;
    price: number;

    constructor(brand: string, model: string, price: number) {
        this.brand = brand;
        this.model = model;
        this.price = price;
    }

    setTime(time: string): void {
        console.log(`${this.brand} ${this.model} - Time set to ${time}`);
    }

    abstract showTime(): void;
}

class SmartP extends WatchP {
    batteryLevel: number = 100;

    constructor(brand: string, model: string, price: number) {
        super(brand, model, price);
    }

    showTime(): void {
        console.log(`${this.brand} ${this.model} - Battery level: ${this.batteryLevel}%`);
    }

    chargeBattery(): void {
        console.log(`${this.brand} ${this.model} - Charging...`);
        this.batteryLevel = 100;
        console.log(`${this.brand} ${this.model} - Battery fully charged.`);
    }
}

class ClassicP extends WatchP {
    style: string;

    constructor(brand: string, model: string, price: number, style: string) {
        super(brand, model, price);
        this.style = style;
    }

    showTime(): void {
        console.log(`${this.brand} ${this.model} - This is a classic watch.`);
    }
}


function showtime(watch: WatchP): void {
    watch.showTime();
}

const smartwatchp = new SmartP("Apple", "Watch Series 6", 399);
const classicWatchp = new ClassicP("Rolex", "Submariner", 10000, "Luxury");


showtime(smartwatchp);
showtime(classicWatchp);
