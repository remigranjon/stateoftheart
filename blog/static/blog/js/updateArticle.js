



const dataToInsert = document.getElementById("dataToInsert");



const editor = new EditorJS ({
    /**
    * Id of Element that should contain Editor instance
    */
   holder: 'editorjs',
   
   tools:{
     header: Header,
     equation: Equation,
     image: {
       class: ImageTool,
       config: {
         endpoints: {
           byFile: 'http://localhost:8000/blog/uploadImage/', // Your backend file uploader endpoint
           byUrl: 'http://localhost:8008/fetchUrl', // Your endpoint that provides uploading by Url
         }
       }
     },
   },
   
   data:JSON.parse(dataToInsert.value),
   // data:{
   //   "time" : 189819819819,
   //   "version" : "2.26.5",
   //   "blocks" : [
   //     {
   //       "type": "header",
   //       "data": {
   //         "text":"Titre 1",
   //         "level" : 2
   //       }
   //     },
   //     {
   //       "type": "paragraph",
   //       "data": {
   //         "text": "lorem ipsum aerouivzae zoefygvz fv zofuvg zrfv zouvygz rfov zo vzrg vozuyg vzorygv ozuyv z"
   //       }
   //     }
   //   ]
   // },
  
 
 })
 
 //  function that creates a form and an input to send data to "blog:saveArticle" url with POST method
function sendDataWithForm (data) {
  // const form = document.createElement("form");
  // form.method= "POST";
  // form.action = document.getElementById("saveUrl").value

  const form = document.getElementById("saveForm")

  const input = document.getElementById("id_data")
  input.value = data;

  form.submit();

}

function saveArticle () {
  editor.save().then((outputData) => {
    sendDataWithForm(JSON.stringify(outputData))
  }).catch((error) => {
    console.log('Saving failed: ', error)
  });
}
 
function addTag (newTagValue) {

  // let newTagValue = document.getElementById('newTag').value;
  const tags = document.getElementsByClassName("tags")[0];
  const tagsInput = document.getElementById("tags");

  const newTag = document.createElement('div');
  const newTagText = document.createElement('p');
  const newTagDelete = document.createElement("button");


  newTag.classList.add("tag");

  // newTagValue = newTagValue.replace(" ","-");

  newTagText.innerHTML = newTagValue;

  // Ajout du tag à l'input "tags"
  tagsInput.value = tagsInput.value + newTagValue + " ";
    
  newTagDelete.innerHTML = 'x';
  newTagDelete.onclick = (event)=>{
    event.preventDefault();
    tags.removeChild(newTag);
    // suppression du tag dans l'input "tags"
    const tagToDelete = " " + newTagValue + " ";
    tagsInput.value = tagsInput.value.replace(tagToDelete, " ");
  }

  tags.appendChild(newTag);
  newTag.appendChild(newTagText);
  newTag.appendChild(newTagDelete);
}

function addTagFromEvent(event) {
  let newTagValue = document.getElementById('newTag').value;
  regex = new RegExp(" ","g");
  newTagValue = newTagValue.replace(regex,"-").toLowerCase();
  addTag(newTagValue);

}


let tagsToAdd = document.getElementById("tagsToAdd").value.split(' ');
tagsToAdd.pop();
console.log(tagsToAdd);

for (let tag of tagsToAdd) {
  console.log(tag);
  addTag(tag);
}