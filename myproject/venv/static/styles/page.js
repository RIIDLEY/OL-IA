function progBarUpdate(){
  var postVal = document.getElementById("commentVal").value
  console.log(postVal);

  //if(document.getElementById("comment").value !== NULL && document.getElementById("commentVal").value !== NULL){
    document.getElementById("div_result").innerHTML = 
    "<section id='section_result'>" +
      "<p style='text-align: center;'>Le commentaire</p>" +
      "<i><p style='text-align: center;' id='commentInput'></p></i>" + 
      "<strong><p style='text-align: center;' id='resultComment'></p></strong>" +
      "<div id='progress_container'>" +
        "<div id='progress_container_text'>" +
          "<div id='progress_container_text_align_center'></div>" +
        "</div>" +
        "<div id='loading_bar'></div>" +
      "</div>" +
    "</section>"
  //}

  var i = 0;

      if (i == 0) {
        i = 1;
        var elem = document.getElementById("loading_bar");
        document.getElementById("commentInput").textContent = document.getElementById("comment").value;
        if(postVal<50){
            //elem.style.backgroundColor = "red";
            document.getElementById("resultComment").textContent = "est NEGATIF!";
        }else{
            //elem.style.backgroundColor = "green";
            document.getElementById("resultComment").textContent = "est POSITIF!";
        }
        var width = 1;
        var id = setInterval(frame, 10);
        function frame() {
          if (width >= postVal) {
            clearInterval(id);
            i = 0;
          } else {
            width++;
            elem.style.width = width + "%";
          }
        }
      }
      document.getElementById("progress_container_text_align_center").textContent = postVal + " %";


}


function addInputComment(){
  var nbInput = parseInt($("#total_comment").val()) + 1;
  console.log(nbInput);
  
  var new_input = "<input type='text' id='comment" + nbInput + "' name='comment" + nbInput + "' placeholder='Commentaire à analyser' required>"//<input type='number' id='commentVal" + nbInput + "' name='commentVal" + nbInput + "' placeholder='Pourcentage retourne du modele' max='100' required>";

  $('#div_comment').append(new_input);
  
  $('#total_comment').val(nbInput);
  
  //document.getElementById("div_comment").insertAdjacentHTML("beforeend","<textarea type='text' id='comment1' name='comment1' placeholder='Commentaire à analyser' required></textarea><input type='number' id='commentVal1' name='commentVal1' placeholder='Pourcentage retourne du modele' max='100' required>");
}

$(document).ready(function(){
  document.getElementById("total_comment").value = 1;
  
});

/*
$(document).ready( function () {
  
    console.log(document.getElementById("progress_container_text_align_center"));
    
    var postId=document.getElementById("fid").value;
    console.log(postId);

    var i = 0;

      if (i == 0) {
        i = 1;
        var elem = document.getElementById("loading_bar");
        if(postId<50){
            elem.style.backgroundColor = "red";
            document.getElementById("resultComment").textContent = "est négatif!";
        }else{
            elem.style.backgroundColor = "green";
            document.getElementById("resultComment").textContent = "est positif!";
        }
        var width = 1;
        var id = setInterval(frame, 10);
        function frame() {
          if (width >= postId) {
            clearInterval(id);
            i = 0;
          } else {
            width++;
            elem.style.width = width + "%";
          }
        }
      }
      document.getElementById("progress_container_text_align_center").textContent = postId + " %";
      
});
*/