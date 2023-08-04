//========================================================================
// Drag and drop image handling
//========================================================================

var fileDrag = document.getElementById("file-drag");
var fileSelect = document.getElementById("file-upload");

// Add event listeners
fileDrag.addEventListener("dragover", fileDragHover, false);
fileDrag.addEventListener("dragleave", fileDragHover, false);
fileDrag.addEventListener("drop", fileSelectHandler, false);
fileSelect.addEventListener("change", fileSelectHandler, false);

function fileDragHover(e) {
  // prevent default behaviour
  e.preventDefault();
  e.stopPropagation();

  fileDrag.className = e.type === "dragover" ? "upload-box dragover" : "upload-box";
}

function fileSelectHandler(e) {
  // handle file selecting
  var files = e.target.files || e.dataTransfer.files;
  fileDragHover(e);
  for (var i = 0, f; (f = files[i]); i++) {
    previewFile(f);
  }
}

//========================================================================
// Web page elements for functions to use
//========================================================================

var imagePreview = document.getElementById("image-preview");
var imageDisplay = document.getElementById("image-display");
var uploadCaption = document.getElementById("upload-caption");
var predResult = document.getElementById("pred-result");
var loader = document.getElementById("loader");

//========================================================================
// Main button events
//========================================================================

function submitImage() {
  // action for the submit button
  console.log("submit");

  if (!imageDisplay.src || !imageDisplay.src.startsWith("data")) {
    window.alert("Please select an image before submit.");
    return;
  }

  loader.classList.remove("hidden");
  imageDisplay.classList.add("loading");

  // call the predict function of the backend
  predictImage(imageDisplay.src);
}

function clearImage() {
  // reset selected files
  fileSelect.value = "";

  // remove image sources and hide them
  imagePreview.src = "";
  imageDisplay.src = "";
  predResult.innerHTML = "";

  hide(imagePreview);
  hide(imageDisplay);
  hide(loader);
  hide(predResult);
  show(uploadCaption);

  imageDisplay.classList.remove("loading");
}

function previewFile(file) {
  // show the preview of the image
  console.log(file.name);
  var fileName = encodeURI(file.name);

  var reader = new FileReader();
  reader.readAsDataURL(file);
  reader.onloadend = () => {
    imagePreview.src = URL.createObjectURL(file);

    show(imagePreview);
    hide(uploadCaption);

    // reset
    predResult.innerHTML = "";
    imageDisplay.classList.remove("loading");

    displayImage(reader.result, "image-display");
  };
}

//========================================================================
// Helper functions
//========================================================================

function predictImage(image) {
  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(image)
  })
    .then(resp => {
      if (resp.ok)
        resp.json().then(data => {
          displayResult(data);
        });
    })
    .catch(err => {
      console.log("An error occured", err.message);
      window.alert("Oops! Something went wrong.");
    });
}

function displayImage(image, id) {
  // display image on given id <img> element
  let display = document.getElementById(id);
  display.src = image;
  show(display);
}

// function displayResult(data) {
//   // display the result
//   // imageDisplay.classList.remove("loading");
//   // hide(loader);
//   // predResult.innerHTML = data.result;
//   document.getElementById('prediction').innerHTML="Predicted Class ID: " + data.result.predicted_class_id+ "Predicted one hot"+ data.result.predicted_one_hot+"Predicted_probability"+data.result.predicted_probability;
//   // show(predResult);
// }
// function displayResult(data) {
//   // Extract the values from the response object
//   var predictedClassId = data.result.predicted_class_id;
//   var predictedOneHotArray = data.result.predicted_one_hot_array;
//   var predictedProbability = data.result.predicted_probability;

//   // Convert the predicted one-hot array to a string
//   var predictedOneHotString = "[" + predictedOneHotArray.join(", ") + "]";

//   // Update the content of the <p> element with id "prediction"
//   document.getElementById('prediction').innerHTML = "Predicted Class ID: " + predictedClassId + "<br>" +
//                                                     "Predicted One-Hot Array: " + predictedOneHotString + "<br>" +
//                                                     "Predicted Probability: " + predictedProbability;
// }
function displayResult(data) {
  // Define a mapping of class IDs to class names
  var classMapping = {
    0: 'Atopic-dermatitis',
    1: 'Lupus-Chronic',
    2: 'Nail-disease',
    3: 'Acne',
    4: 'Actinic',
    5: 'Allergic-Contact-Dematitis',
    6: 'Alopecia',
    7: 'Atypical-Nevi',
    8: 'Basal-Cell',
    9: 'Bullous',
    10: 'Cellulitis',
    11: 'Drug Eruptions',
    12: 'Eczema',
    13: 'Erythema-multiforme',
    14: 'Exanthems',
    15: 'Hemangioma',
    16: 'Herpes STDs',
    17: 'Hives-Urticaria',
    18: 'Licheen-Planus',
    19: 'Light-Disease',
    20: 'molluscum-Contagiosum',
    21: 'Psoriasis',
    22: 'Pyogenic',
    23: 'Rosacea',
    24: 'Scabies',
    25: 'Seborrheic',
    26: 'tinea-Ringworm',
    27: 'Vasculitis',
    28: 'Warts'

  };

  // Extract the values from the response object
  var predictedClassId = data.result.predicted_class_id;
  var predictedOneHotArray = data.result.predicted_one_hot_array;
  var predictedProbability = data.result.predicted_probability;

  // Get the predicted class name from the class mapping
  var predictedClassName = classMapping[predictedClassId];

  // Convert the predicted one-hot array to a string
  var predictedOneHotString = "[" + predictedOneHotArray.join(", ") + "]";

  // Update the content of the <p> element with id "prediction"
  document.getElementById('prediction').innerHTML = "Predicted Class: " + predictedClassName + "<br>" +
                                                    "Predicted Probability: " + predictedProbability*100+'%' + "<br>" +
                                                    "Class Probabilities: " +'<br>'+ Object.keys(classMapping).map(function(classId) {
                                                      return classMapping[classId] + "  :  " + (data.result.predicted_one_hot_array[0][classId]*100).toFixed(4)+'%'+'<br>';
                                                    }).join("");
}

// function displayResult(data) {
//   // Extract the values from the response object
//   var predictedClassId = data.result.predicted_class_id;
//   var predictedOneHotArray = data.result.predicted_one_hot_array;
//   var predictedProbability = data.result.predicted_probability;

//   // Map class IDs to class names
//   var classNames = ["class1", "class2", "class3", "class4"]; // Update with your actual class names

//   // Get predicted class name
//   var predictedClassName = classNames[predictedClassId - 1];

//   // Convert predicted one-hot array to string
//   var classProbabilities = "";
//   for (var i = 0; i < predictedOneHotArray.length; i++) {
//     classProbabilities += classNames[i] + ": " + predictedOneHotArray[i] + ", ";
//   }
//   classProbabilities = classProbabilities.slice(0, -2); // Remove trailing comma and space

//   // Update the content of the <p> element with id "prediction"
//   document.getElementById('prediction').innerHTML = "Predicted Class: " + predictedClassName + "<br>" +
//                                                     "Predicted Probability: " + predictedProbability + "<br>" +
//                                                     "Class Probabilities: " + classProbabilities;
// }



function hide(el) {
  // hide an element
  el.classList.add("hidden");
}

function show(el) {
  // show an element
  el.classList.remove("hidden");
}