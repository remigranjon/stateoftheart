class Equation {
    static get toolbox() {
        return {
            title: 'Equation',
            icon: '<svg fill="#000000" width="800px" height="800px" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg"><path d="M1919.989 168.955V394.95h-832.716l-476.16 1251.388-212.78-4.743-194.373-588.537H-.01V827.176h285.515l107.294 77.59L513.08 1268.89 903.857 241.802l105.6-72.847h910.532ZM1265.72 788.99l240.177 240.176 240.162-240.12 159.7 159.586-240.2 240.197 240.2 240.198-159.7 159.586-240.163-240.12-240.176 240.177-159.698-159.7 240.183-240.141-240.183-240.14 159.698-159.7Z" fill-rule="evenodd"/></svg>'
        };
    }
    
    constructor({data}){
        this.data = data;
    }

    render(){
        const wrapper = document.createElement('div');
        wrapper.style.display = "flex";
        wrapper.style.flexDirection = "column";
        wrapper.style.gap = "15px";
        wrapper.style.marginBottom = "20px";
        wrapper.style.marginTop = "20px";

        const inputEquation = document.createElement('input');
        inputEquation.style.width = "100%";
        inputEquation.style.outline = "none";
        inputEquation.style.padding = "10px";
        inputEquation.placeholder = "Enter your equation as LaTex language";
        inputEquation.classList.add("inputEquation");
        if (this.data.equation) {
            inputEquation.value = this.data.equation
        }

        const inputCaption = document.createElement('input');
        inputCaption.style.width = "100%";
        inputCaption.style.outline = "none";
        inputCaption.style.padding = "10px";
        inputCaption.placeholder = "Caption";
        inputCaption.classList.add("inputCaption");
        if (this.data.caption) {
            inputCaption.value = this.data.caption
        }

        wrapper.appendChild(inputEquation);
        wrapper.appendChild(inputCaption);

        return wrapper;
    }
    save(blockContent) {
        const inputEquation = blockContent.getElementsByClassName("inputEquation")[0];
        const inputCaption = blockContent.getElementsByClassName("inputCaption")[0];
        
        return {
            equation: inputEquation.value,
            caption: inputCaption.value
        }
    }
}