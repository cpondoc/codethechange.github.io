<template>
<div class = "page">

    <div class = "header-container">
        <div class = "header-group">
            <h1 class = "header-title">Change the world and build projects with us.</h1>
            <div class = "cta-button">
                <a href="https://codethechange.typeform.com/to/w7qJSt"
                  target="_blank"
                ><h3> JOIN </h3></a>
                <div id = "button-arrow">  </div>
            </div>
        </div>
    </div>

    <div class = "container-right">
        <div class = "cr-image">
            <img id="code-img" src="@/assets/img/code@2x.png"/>
         </div>
        <div class = "cr-text">
            <h2 id = "code-h2">Make code your superpower…</h2>
            <p  id = "code-p">Improve your software development skills while improving the world, one project at a time.</p>
        </div>
    </div>

    <div class = "container-left">
        <div class = "content-left">
        <div class = "cl-text">
            <h2>unless your superpower is design.</h2>
            <p>Improve your design skills while ensuring that our projects are impactful, useful, and delightful.</p>
        </div>
        <div class = "cl-image">
        <img id="design" src="@/assets/img/sketch@2x.png" />
        <img id="bg" src="@/assets/img/ctc-background@2x.png" />
        </div>
        </div>
    </div>

    <div class = "container-right">
         <div class = "cr-image">
            <img id="family" src="@/assets/img/family@2x.png" >
         </div>

        <div class = "cr-text">
            <h2 id = "family-h2" >You’re joining a family</h2>
            <p id = "family-p">Learn and grow in a supportive community with workshops and project mentors.</p>
        </div>
    </div>

    <div class = "cta">
        <h1> Want to stay in the loop? Sign up for our mailing list!</h1>
        <div class = "cta-button" id ="footer-cta">
             <a
               href="https://mailman.stanford.edu/mailman/listinfo/codethechange_general"
               target="_blank"
             ><h3> Sign Up </h3></a>
        </div>
    </div>
</div>

</template>
<script>
export default {
}
</script>

<style lang="scss" scoped>
@import '../theme.scss';

a {
    text-decoration: none;
}

.row {
    margin: 0px;
    padding: 0px;
}

.header-container{
  width: 100%;
  height: 55vh;
  background-color: $secondary-light;

}

.header-group{
  font-family: OpenSans;
  padding-left: 10em;
  padding-right: 10em;
  padding-top: 8em;
  padding-bottom: 10em;

}

.header-title{
  font-family: Comfortaa;
  font-size: 3.5em;
    font-weight: bold;
  line-height: 1.39;
  letter-spacing: normal;
  color: $secondary-medium;
}
.cta-button{
  margin-top: 4em;
  width: 21vw;
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

.container-right{
    display: flex;
    flex-direction: row;
    padding-bottom: 7em;
    width: 100%;
}

.cr-image{
        flex: 50%;
        padding-top: 7em;

}
.cr-text{
    flex: 50%;
    text-align: left;
    padding-top: 15em;
    padding-left: 6em;
}

h2{
    font-family: Comfortaa;
    font-weight: 800;
    font-size: 2.2em;
    padding-bottom: 1vh;
    width: 40vw;
}

p{
    font-size: 1.1em;
    font-weight: normal;
    font-style: normal;
    font-stretch: normal;
    line-height: 2.14;
    letter-spacing: normal;
    width: 35vw;
}

#code-h2{
    color:white;

}

#code-p{
    color: #bfbfbf;

}

#code-img{
height: 60vh;
width: 49vw;
}

.container-left{
    background-color: white;
    overflow: hidden;
}

.cl-image{
    flex: 50%;
    position: relative;
}

.cl-text{
    flex: 50%;
    text-align: left;
    color: black;
    padding-top: 15em;
    padding-left: 6em;

}

.cl-text p{
    color: #696969;
}

#bg{
    width: 55vw;
    height: 85vh;
}

#design{
    position: absolute;
    width: 45vw;
    height: 70vh;
    top: 12%;
    left: 9%;
}

.content-left{
    display: flex;
    flex-direction: row;

}

#family{
    width: 45vw;
    height: 70vh;
}

.cta{
    width:100%;
    background-color: #252525;
    text-align: center;
    padding: 10em;
}

#footer-cta{
    display: inline-block;
    text-align:center;
    margin-left: auto;
    margin-right: auto;

}

.cta h1{
    color: $secondary-light;
}

</style>
