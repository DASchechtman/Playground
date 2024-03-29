let size = 100000
let x = new Array<Array<number>>(size).fill(new Array<number>(size).fill(Math.round(Math.random())))

function roughSizeOfObject(object: any) {
    const objectList: any = [];
    const stack = [object];
    let bytes = 0;

    while (stack.length) {
        const value = stack.pop();

        switch (typeof value) {
            case 'boolean':
                bytes += 4;
                break;
            case 'string':
                bytes += value.length * 2;
                break;
            case 'number':
                bytes += 8;
                break;
            case 'object':
                if (!objectList.includes(value)) {
                    objectList.push(value);
                    for (const prop in value) {
                        if (value.hasOwnProperty(prop)) {
                            stack.push(value[prop]);
                        }
                    }
                }
                break;
        }
    }

    return bytes;
}

console.log(roughSizeOfObject(x))
let mem_size = 0
for (let are of x) {
    mem_size += are.length
}

console.log(mem_size)
