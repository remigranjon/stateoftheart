// import EditorJS from './editor';
// import Header from './editor';
// import List from './editor';

const editor = new EditorJS ({
   /**
   * Id of Element that should contain Editor instance
   */
  holder: 'editorjs',
  
  placeholder: 'Write...',

  tools:{
    header: Header,
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

  // console.log(input.value);
  form.submit();

}

function saveArticle () {
  editor.save().then((outputData) => {
    sendDataWithForm(JSON.stringify(outputData))
  }).catch((error) => {
    console.log('Saving failed: ', error)
  });
}


document.getElementById("id_title").setAttribute("spellcheck", "false")
document.getElementById("id_abstract").setAttribute("spellcheck", "false")