<template>
<div class = "page">

    <div class = "header-container">
        <div class = "header-group">
            <h1 class = "header-title">Change the world and build projects with us.</h1>
            <div class = "cta-button"> 
                <h3> APPLY </h3>
                <div id = "button-arrow">  </div>
            </div>
        </div>
    </div>

    <div class = "container-right">
        <div class = "cr-image">
         <img id="code-img" src="@/assets/img/code@2x.png" > 
         </div>
        <div class = "cr-text">
            <h2 id = "code-h2">Make code your superpower…</h2>
            <p  id = "code-p"> Technical leadership and support from Stanford student volunteers dedicating 5 to 10 hours per week on the project free of cost. </p>
        </div>
    </div>

    <div class = "container-left">
        <div class = "content-left">
        <div class = "cl-text">
            <h2>unless your superpower is design.</h2>
            <p>Technical leadership and support from Stanford student volunteers dedicating 5 to 10 hours per week on the project free of cost. </p>
        </div>
        <div class = "cl-image">
        <img id="design" src="@/assets/img/sketch@2x.png" />
         <img id="bg" src="@/assets/img/ctc-background@2x.png" />
        </div>
        </div>
    </div>

    <div class = "container-right">
        <div class = "cr-text">
            <h2 id = "family-h2" >You’re joining a family</h2>
            <p id = "family-p">We built a project matching platform that boosted engagement by 60%.   We’re Code the Change, a club at Stanford University that builds useful software for high-impact nonprofits.  </p>
        </div>
        <img id="family" src="@/assets/img/family@2x.png" />

    </div>

    <div class = "cta">
        <h1> Ready to jump in?  Apply today. </h1>
        <div class = "cta-button"> 
                    <h3> Apply </h3>
                     <div id = "button-arrow">
                    </div>
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

.page{
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
  padding-top: 5em;
}

.header-title{
  font-family: Comfortaa;
  font-size: 4em;
    font-weight: bold;
  line-height: 1.39;
  letter-spacing: normal;
  color: $secondary-medium;
}
.cta-button{
    margin-top: 5em;
width: 349px;
  height: 73px;
  border-radius: 8px;
  box-shadow: 0 4px 25px 0 rgba(252, 85, 85, 0.5);
  background-color: $secondary-heavy;
}

.cta-button h3{
    font-family: "Open Sans";
  font-size: 21px;
  font-weight: 800;
  font-style: normal;
  font-stretch: normal;
  line-height: 3.57;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
}

#button-arrow{

}

.container-right{
    display: flex;
    flex-direction: row;
    padding-bottom: 7em;
    width: 100%;

}

.cr-image{
        flex: 50%;    
        padding-top: 10em;

}
.cr-text{
    flex: 50%;
    text-align: left;
    padding-top: 20em;
    padding-left: 6em;

}

h2{
      font-family: Comfortaa;
      font-weight: 800;
          font-size: 2.4em;
          padding-bottom: 1vh;
}

p{
     font-size: 1.1em;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 2.14;
  letter-spacing: normal;

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
}

.cl-image{
    flex: 50%;
    position: relative;
}

.cl-text{
    flex: 50%;
    text-align: center;
    color: black;
    padding-top: 15em;
    padding-left: 6em;

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

</style>
