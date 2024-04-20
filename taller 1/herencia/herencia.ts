class Watch {
    brand: string;
    model: string;
    price: number;

    constructor(brand: string, model: string, price: number) {
        this.brand = brand;
        this.model = model;
        this.price = price;
    }

    setTime(time: string): void {
        console.log(`Time set to ${time}`);
    }
}

class BSmart extends Watch {
    features: string[];

    constructor(brand: string, model: string, price: number, features: string[]) {
        super(brand, model, price);
        this.features = features;
    }

    checkHeartRate(): void {
        console.log("Checking heart rate...");
        console.log("Your heart rate is 75 bpm.");
    }
}

class BClassic extends Watch {
    style: string;

    constructor(brand: string, model: string, price: number, style: string) {
        super(brand, model, price);
        this.style = style;
    }

    setTime(time: string): void {
        console.log(`Time set to ${time}`);
    }
}

const smartwatch = new BSmart("Apple", "Watch Series 6", 399, ["Heart Rate Monitor", "GPS"]);
smartwatch.checkHeartRate();

const classicWatch = new BClassic("Rolex", "Submariner", 10000, "Luxury");
classicWatch.setTime("10:30 AM");
