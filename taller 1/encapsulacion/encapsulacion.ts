abstract class WatchC {
    brand: string;
    model: string;
    price: number;
    private isOn: boolean = false;

    constructor(brand: string, model: string, price: number) {
        this.brand = brand;
        this.model = model;
        this.price = price;
    }

    setTime(time: string): void {
        if (this.isOn) {
            console.log(`${this.brand} ${this.model} - Time set to ${time}`);
        } else {
            console.log(`${this.brand} ${this.model} is turned off.`);
        }
    }

    turnOn(): void {
        this.isOn = true;
        console.log(`${this.brand} ${this.model} - Turned on.`);
        this.start();
    }

    turnOff(): void {
        this.isOn = false;
        console.log(`${this.brand} ${this.model} - Turned off.`);
        this.stop();
    }

;

    private start(): void {
        console.log(`${this.brand} ${this.model} - Starting...`);
    }

    private stop(): void {
        console.log(`${this.brand} ${this.model} - Stopping...`);
    }
}

class SmartC extends WatchC {
    batteryLevel: number = 100;

    constructor(brand: string, model: string, price: number) {
        super(brand, model, price);
    }



    chargeBattery(): void {
        console.log(`${this.brand} ${this.model} - Charging...`);
        this.batteryLevel = 100;
        console.log(`${this.brand} ${this.model} - Battery fully charged.`);
    }

    private linkDevice(): void {
        console.log(`${this.brand} ${this.model} - Smart specific function.`);
    }
}

class ClassicC extends WatchC {
    style: string;

    constructor(brand: string, model: string, price: number, style: string) {
        super(brand, model, price);
        this.style = style;
    }

    private changeBattery(): void {
        console.log(`${this.brand} ${this.model} - Classic specific function.`);
    }
}


const smartwatch = new SmartC("Apple", "Watch Series 6", 399);
smartwatch.turnOn();
smartwatch.setTime("10:30 AM");
smartwatch.chargeBattery();
smartwatch.turnOff();

const classicWatch = new ClassicC("Rolex", "Submariner", 10000, "Luxury");
classicWatch.turnOn();
classicWatch.setTime("10:30 AM");
classicWatch.turnOff();
