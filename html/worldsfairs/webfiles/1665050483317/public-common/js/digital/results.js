function getElementsByClassName(searchClass,tag,node) {
   var classElements = new Array();
   if (node == null)
      node = document;
   if (tag == null)
      tag = '*';
   var els = node.getElementsByTagName(tag);
   var elsLen = els.length;
   var pattern = new RegExp("(^|\\s)"+searchClass+"(\\s|$)");
   for (i = 0, j = 0; i < elsLen; i++) {
      if (pattern.test(els[i].className) ) {
         classElements[j] = els[i];
         j++;
      }
   }
   return classElements;
}

 function redirectToURL(btnId, link) {
	 history.pushState(null, null, '#part='+btnId);
	 var selection = document.querySelector(".active");
	 if(selection) selection.className = "";
	 document.querySelector(".play").setAttribute('href', link);
	 document.querySelector(".object-part").innerHTML = "Part "+btnId;
	 document.querySelector("#button"+btnId).className = "active"
 }

function getElementsByAttribute(oElm, strTagName, strAttributeName, strAttributeValue) {
   var arrElements = (strTagName == "*" && document.all)? document.all : oElm.getElementsByTagName(strTagName);
   var arrReturnElements = new Array();
   var oAttributeValue = (typeof strAttributeValue != "undefined")? new RegExp("(^|\\s)" + strAttributeValue + "(\\s|$)") : null;
   var oCurrent;
   var oAttribute;
   for(var i=0; i<arrElements.length; i++){
      oCurrent = arrElements[i];
      oAttribute = oCurrent.getAttribute(strAttributeName);
      if(typeof oAttribute == "string" && oAttribute.length > 0){
         if(typeof strAttributeValue == "undefined" || (oAttributeValue && oAttributeValue.test(oAttribute))){
            arrReturnElements.push(oCurrent);
         }
      }
   }
   return arrReturnElements;
}


function init() {
   try {
      document.sortResults.reset();
      document.selectFacets.reset();
      document.pageNav.reset();
      document.showPerPage.reset();
      var refineSearch = document.getElementById("refineSearch");
      var fieldsets = getElementsByClassName("fields","div");
      for (var i = 0; i < fieldsets.length; i++) {
         var showHide = getElementsByClassName("showHide","div",fieldsets[i])[0];
         showHide.style.display = "block";
         var checkboxes = getElementsByAttribute(fieldsets[i],"input","type","checkbox");
         var textboxes = getElementsByAttribute(fieldsets[i],"input","type","text");
         var radioboxes = getElementsByAttribute(fieldsets[i],"input","type","radio");
         var selectboxes = fieldsets[i].getElementsByTagName("select");
         var checked = 0;
         for (var j = 0; j < checkboxes.length; j++) {
            if (checkboxes[j].checked) {
               checked++;
               break;
            }
         }
         if (checked == 0) {
            for (var q = 0; q < textboxes.length; q++) {
               if (textboxes[q].value.length > 0) {
                  checked++;
                  break;
               }
            }
         }
         if (checked == 0) {
            for (var r = 0; r < radioboxes.length; r++) {
               if (radioboxes[r].checked && radioboxes[r].value.length > 0) {
                  checked++;
                  break;
               }
            }
         }
         
         if (checked > 0 || selectboxes.length > 0) {
            showFields(fieldsets[i]);
         } else {
            hideFields(fieldsets[i]);
         }
      }
   } catch (e) {
      // Nothing to do...
   }
}

function hideFields(fieldset) {
   var showHide = getElementsByClassName("showHide","div",fieldset)[0];
   var show = getElementsByClassName("show","span",showHide)[0];
   var hide = getElementsByClassName("hide","span",showHide)[0];
   var labels = fieldset.getElementsByTagName("label");
   var checkboxes = getElementsByAttribute(fieldset,"input","type","checkbox");
   var textboxes = getElementsByAttribute(fieldset,"input","type","text");
   for (var l = 0; l < checkboxes.length; l++) {
      checkboxes[l].disabled = true;
   }
   for (var o = 0; o < textboxes.length; o++) {
      textboxes[o].disabled = true;
   }
   for (var k = 0; k < labels.length; k++) {
      labels[k].style.display = "none";
   }
   hide.style.display = "none";
   show.style.display = "inline";
}

function showFields(fieldset) {
   var showHide = getElementsByClassName("showHide","div",fieldset)[0];
   var show = getElementsByClassName("show","span",showHide)[0];
   var hide = getElementsByClassName("hide","span",showHide)[0];
   var labels = fieldset.getElementsByTagName("label");
   var checkboxes = getElementsByAttribute(fieldset,"input","type","checkbox");
   var textboxes = getElementsByAttribute(fieldset,"input","type","text");
   for (var m = 0; m < checkboxes.length; m++) {
      if (checkboxes[m].parentNode.className.indexOf("forceDisabled") == -1) {
         checkboxes[m].disabled = false;
      }
   }
   for (var p = 0; p < textboxes.length; p++) {
      textboxes[p].disabled = false;
   }
   for (var n = 0; n < labels.length; n++) {
      labels[n].style.display = "block";
   }
   hide.style.display = "inline";
   show.style.display = "none";
}
