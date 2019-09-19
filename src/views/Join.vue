<template>
<div class="page">

    <div class="header-container">
        <div class="header-group">
            <h1 class="header-title">Change the world and build projects with us.</h1>
            <div class="cta-button">
                <a href="https://codethechange.typeform.com/to/UZmRwu"
                   target="_blank"
                ><h3> JOIN </h3></a>
                <div id="button-arrow">  </div>
            </div>
        </div>
    </div>

    <div class="container-right">
      <div class="cr-image container-image">
        <img id="code-img" src="@/assets/img/code@2x.png"/>
      </div>
      <h2 id="code-h2 container-title">Make code your superpower…</h2>
      <p  id="code-p container-text">Improve your software development skills while improving the world, one project at a time.</p>
    </div>

    <div class="container-left">
        <h2 id="design-h2" class="container-title">unless your superpower is design.</h2>
        <p id="design-p" class="container-text">Improve your design skills while ensuring that our projects are impactful, useful, and delightful.</p>
        <div class="cl-image container-image">
          <img id="design" src="@/assets/img/sketch@2x.png" />
          <img id="bg" src="@/assets/img/ctc-background@2x.png" />
        </div>
    </div>

    <div class="container-right">
         <div class="cr-image container-image">
            <img id="family" src="@/assets/img/family@2x.png" >
         </div>
        <h2 id="family-h2" class="container-title">You’re joining a family</h2>
        <p id="family-p" class="container-text">Learn and grow in a supportive community with workshops and project mentors.</p>
    </div>

    <div class="cta">
        <h1 class="cta-title"> Want to stay in the loop? Sign up for our mailing list!</h1>
        <div class="cta-button" id ="footer-cta">
             <a
               href="https://mailman.stanford.edu/mailman/listinfo/codethechange_general"
               target="_blank"
             ><h3> Sign Up </h3></a>
        </div>
    </div>
</div>
</template>

<style lang="scss" scoped>
@import '../theme.scss';

a {
  text-decoration: none;
}

.header-container{
  width: 100%;
  background-color: $secondary-light;
}

.header-group{
  font-family: OpenSans;
  padding-left: 10em;
  padding-right: 10em;
  @media only screen and (max-width: 700px) {
    padding-left: 2em;
    padding-right: 2em;
  }
  padding-top: 8em;
  padding-bottom: 5em;
}

.header-title{
  font-family: Comfortaa;
  font-size: 3.5em;
    font-weight: bold;
  @media only screen and (max-width: 700px) {
    font-size: 2em;
    line-height: 70px;
  }
  line-height: 1.39;
  letter-spacing: normal;
  color: $secondary-medium;
}
.cta-button{
  margin-top: 4em;
  width: 200px;
  height: 7.5vh;
  border-radius: 8px;
  box-shadow: 0 4px 25px 0 rgba(252, 85, 85, 0.5);
  background-color: $secondary-heavy;
  &:hover{
    background-color: #CF6969;
    cursor: pointer;
    -webkit-box-shadow: 0 2px 9px 0 rgba(0,0,0,.2);
    box-shadow: 0 4px 45px 0 rgba(252, 85, 85, 0.5);
    -webkit-transform: translateY(-1px) scale(1.01);
    transform: translateY(-1px) scale(1.01);
  }
}

.cta-button h3{
  font-family: "Open Sans";
  font-size: 1.3em;
  font-weight: 1000;
  font-style: normal;
  font-stretch: normal;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
  margin-top: auto;
  margin-bottom: auto;
  text-transform: uppercase;
  line-height: 7.5vh;
  box-sizing: border-box;
  text-decoration: none;
}

h2 {
  font-family: Comfortaa;
  font-weight: 800;
  font-size: 2.2em;
  @media only screen and (max-width: 700px) {
    font-size: 20px;
  }
  padding-bottom: 1vh;
  width: 100%;
}

p {
  font-size: 1.1em;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 2.14;
  letter-spacing: normal;
  width: 100%;
}

.container-right{
  display: grid;
  grid-column-gap: 10%;
  grid-row-gap: 10%;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
    "image title"
    "image text";
  @media only screen and (max-width: 700px) {
    grid-template-columns: 1fr;
    grid-template-areas:
      "title"
      "image"
      "text";
  }
  align-items: center;
  padding-bottom: 7em;
  padding-top: 7em;
  padding-left: 5%;
  padding-right: 5%;
  width: 100%;
}

.container-image {
  grid-area: image;
}

.container-title {
  grid-area: title;
}

.container-text {
  grid-area: text;
}

#code-h2{
  color:white;
}

#code-p{
  color: #bfbfbf;
}

#code-img{
  height: 100%;
  width: 100%;
}

.container-left{
  display: grid;
  align-items: center;
  grid-column-gap: 10%;
  grid-row-gap: 10%;
  grid-template-columns: 1fr 1fr;
  grid-template-areas:
    "title image"
    "text image";
  @media only screen and (max-width: 700px) {
    grid-template-columns: 1fr;
    grid-template-areas:
      "title"
      "image"
      "text";
  }
  padding-left: 5%;
  padding-right: 5%;
  padding-bottom: 7em;
  padding-top: 7em;
  background-color: white;
  width: 100%;
  overflow: hidden;
}

.cl-image{
    position: relative;
}

#design-p {
    color: #696969;
}

#design-h2 {
  color: black;
}

#bg {
  width: 100%;
  height: 100%;
}

#design{
  position: absolute;
  width: 80%;
  height: 80%;
  top: 12%;
  left: 9%;
}

#family{
  width: 100%;
  height: 100%;
}

.cta{
  width:100%;
  background-color: #252525;
  padding: 10em;
  @media only screen and (max-width: 700px) {
    padding: 2em;
  }
}

.cta-title{
  color: $secondary-light;
  @media only screen and (max-width: 700px) {
    font-size: 2em;
    line-height: 70px;
  }
}

</style>
