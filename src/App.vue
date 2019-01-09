<template>
  <div id="app">
    <div class="nav-container">
      <router-link id="logo" to="/"><img id = "logo-styling" src="@/assets/img/logo@2x.png"/></router-link>
      <div id="links">
        <div class = "text-group">
        <router-link class="hover-text link-text" to="/people">people</router-link>
        <router-link class="hover-text link-text" to="/projects">projects</router-link>
        <router-link class="hover-text link-text" to="/partner">partner</router-link>
        </div>
        <div class = "cta-group">
        <router-link id="join-link" class="hover-text link-text" to="/join" >join</router-link>
        </div>
      </div>
    </div>
    <hr id="scroll-shadow" />
    <router-view id="page"/>
    <div id="footer">
      <div class="link-list">
        <p class="link-header">for students</p>
        <hr class="link-line" />
        <router-link class="hover-text small-link-text" to="/people">people</router-link>
        <br /> <br />
        <router-link class="hover-text small-link-text" to="/projects">projects</router-link>
        <br /> <br />
        <router-link class="hover-text small-link-text" to="/join" id="join-small-link">join</router-link>
        <br /> <br />
      </div>
      <div class="link-list">
        <p class="link-header">for organizations</p>
        <hr class="link-line" />
        <router-link class="hover-text small-link-text" to="/partner">partner</router-link>
        <br /> <br />
      </div>
    </div>
  </div>
</template>
<script>
import 'bootstrap'

export default {
  name: 'App'
}
</script>
<style lang="scss">
@import './theme.scss';

*, *::before, *::after {
  box-sizing:border-box
}

.nav-container {
  position: sticky;
  top: -8px;
  z-index: 5;
  background-color: $main-dark;
  padding: 25px;
  width: 100vw;
  display: flex;
  justify-content: space-between;
}

/* Heavily inspired from https://stijndewitt.com/2018/06/12/pure-css-drop-shadow-on-scroll/ */
#scroll-shadow {
  width: 100%;
  height: 10px;
  /* make pseudo elements sticky as well */
  position: sticky;
  top: 50px;
  z-index: 1000;
  box-shadow: 0 2px 19px 0 rgba(124, 124, 124, 0.5);
  z-index: 3;
  margin-top: -25px;
}

.hover-text {
    position: relative;
    text-decoration: none;
    &:hover {
      text-decoration: none;
      color: $accent-light !important;
    }
}

body {
  background-color: $main-dark;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #ffffff;
  background-color: $main-dark;
}

.link-line {
  background-color:$accent-light;
  height: 2px;
}

.small-link-text {
  font-family: Comfortaa;
  font-size: 24px;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: left;
  color: #ffffff;
}

#footer {
  width: 100vw;
  padding-top: 50px;
  display: flex;
  background-color: $main-dark;
}

.link-list {
  margin-left: 85px;
}

.link-header {
  font-family: Comfortaa;
  font-size: 24px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
}

#join-link {
  border-style: solid;
  border-radius: 8px;
  border-width: 2px;
  border-color: white;
  padding-top: 0.7em;
  padding-bottom: 0.7em;
  padding-left: 1.3em;
  padding-right: 1.3em;

  &:hover{
    border-color: $accent-light;
}
}

#logo {
  margin-left: 100px;
}

#logo-styling{
  height: 2.1em;
  width: 2.1em;
}

.link-text {
  font-family: Comfortaa;
  font-size: 18px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
  padding-right:3em;

}

#links {
  margin-right: 80px;
  width: 800px;
  display: flex;
  justify-content: space-around;
  margin-top: 0.6em;
}

.text-group{
  padding-left: 20em;
}
</style>
