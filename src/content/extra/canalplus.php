<?php


  /*
     Send everything to the client and use Js client-side to display everything.
     => The XML is parsed and looped over only once.
  */

  //$SCRIPT_URL = 'http://' . $_SERVER['HTTP_HOST'] . explode('?', $_SERVER['REQUEST_URI'], 2)[0];
  $URL = 'http://service.canal-plus.com/video/rest/search/cplus/petit';
  $SUBTITLE_LENGTH = 18;
  $xml = simplexml_load_file($URL);
  if($xml->count() == 0) {
    echo "An error occured.";
  } else {

    // Get the sections list and sort videos according to
    // the section they belong to.
    $rubriques = array();
    $by_rubrique = array();
    foreach($xml->VIDEO as $video) {
      $rubrique = (string)$video->RUBRIQUAGE->RUBRIQUE;
      if(!in_array($rubrique, $rubriques)) {
        $by_rubrique[$rubrique] = array();
        $rubriques[] = $rubrique;
      }
      $by_rubrique[$rubrique][] = $video;
    }
  }

  function showLink($url, $label_color, $float, $text) {
    if(empty($url)) {
      echo "<a href=\"\" class=\"label label-default\" style=\"float: $float\">$text</a>\n";
    } else {
      echo "<a href=\"$url\" class=\"label label-$label_color\" style=\"float: $float\">$text</a>\n";
    }
  }

?>

<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta http-equiv="Content-type" content="text/html;charset=UTF-8">
    <title>Canal+ videos</title>
    <meta name="description" content="Voir les vidéos Canal+ via RMTP">
    <meta http-equiv="Content-Language" content="fr">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.0.3/css/bootstrap.min.css">
    <script type="text/javascript">
      var displaySection = function() {
        // Hide the current section if one is displayed
        if(typeof(currentSection) != 'undefined') {
          document.getElementById(currentSection).style.display = 'none';
        }
        // Update the current section
        currentSection = document.getElementById('rubrique').value;
        // Show the (new) current section
        document.getElementById(currentSection).style.display = 'block';
      }
    </script>
    <style>
      .thumb_title {
        font-size: 14px;
      }
      .thumb_subtitle {
        font-size: 12px;
      }
      .thumbnail {
        position: relative;
      }
      .thumbnail:hover {
        border-color: #428BCA;
      }

      .thumbnail:hover legend {
        text-decoration: underline;
      }
/*
      legend:hover {
        text-decoration: underline;
      }
*/
      .descr {
        position:absolute;
        bottom:0px;
        left:0px;  
        width:145px;
        margin-left: 9px;
        margin-bottom: 4px;
        margin-right: 0px;
        /* styling */  
        /*background-color:black;*/
        background-color:rgba(0,0,0,0.5);
        font-family: 'tahoma';  
        font-size:15px;  
        color:white;
        /*
        opacity:0.6;
        filter:alpha(opacity=60);
        */
      }
      .descr_content {
        padding:10px;
      }
      .descr_content a {
        text-decoration: none;
        margin: 0;
      }
    </style>
  </head>
  <body onload="displaySection()">

    <div class="container">
      <div class="page-header">
        <h1>Canal+ Videos</h1>
      </div>

      <p>
      <select class="form-control" id="rubrique" onchange="displaySection()">
      <?php
        foreach($rubriques as $rubrique) {
          if($rubrique == "LE_PETIT_JOURNAL") {
            echo "<option selected=\"selected\" value=\"$rubrique\">" . str_replace('_', ' ', $rubrique) . "</option>";
          } else {
            echo "<option value=\"$rubrique\">" . str_replace('_', ' ', $rubrique) . "</option>";
          }
        }
      ?>
      </select>
      </p>


      <?php
        foreach($by_rubrique as $rubrique_name=>$videos) {
          echo "<div class=\"row\" id=\"$rubrique_name\" style=\"display: none\">";
          foreach($videos as $video) {
      ?>
            <div class="col-lg-2 col-sm-4 col-6">
              <span class="thumbnail">
                <legend>
                  <span class="thumb_title"><?php echo $video->INFOS->PUBLICATION->DATE ?></span>
                  <br />
                  <span class="thumb_subtitle">
                  <?php
                    echo str_replace('_', ' ', substr($video->RUBRIQUAGE->CATEGORIE, 0, $SUBTITLE_LENGTH));
                    if(strlen($video->RUBRIQUAGE->CATEGORIE) > $SUBTITLE_LENGTH) {
                      echo '...';
                    }
                  ?>
                  </span>
                </legend>
                <img src="<?php echo $video->MEDIA->IMAGES->PETIT ?>" class="img-rounded">
                <div class="descr">
                  <p class="descr_content">
                    <?php
                      showLink($video->MEDIA->VIDEOS->BAS_DEBIT, 'primary', 'left', 'Low');
                      showLink($video->MEDIA->VIDEOS->HAUT_DEBIT, 'success', 'right', 'High');
                      echo '<br />';
                      showLink($video->MEDIA->VIDEOS->HD, 'warning', 'left', 'HD');
                      showLink($video->MEDIA->VIDEOS->MOBILE, 'danger', 'right', 'Mobile');
                    ?>
                  </p>
                </div>
              </span>
            </div>
      <?php
          }
          echo '</div>';
        }
      ?>
    </div>
  </body>
</html>
