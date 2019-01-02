<template>
  <div id="app">
    <div class="nav-container">
      <router-link id="logo" to="/">LOGO</router-link>
      <div id="links">
        <div class = "text-group">
        <router-link class="underline-text link-text" to="/people">people</router-link>
        <router-link class="underline-text link-text" to="/projects">projects</router-link>
        <router-link class="underline-text link-text" to="/partner">partner</router-link>
        </div>
        <div class = "cta-group">
        <router-link id="join-link" class="underline-text link-text" to="/join" >join</router-link>
        </div>
      </div>
    </div>
    <router-view/>
    <div id="footer">
      <div class="link-list">
        <p class="link-header">for students</p>
        <hr class="link-line" />
        <router-link class="underline-text small-link-text" to="/people">people</router-link>
        <br /> <br />
        <router-link class="underline-text small-link-text" to="/projects">projects</router-link>
        <br /> <br />
        <router-link class="underline-text small-link-text" to="/join" id="join-small-link">join</router-link>
        <br /> <br />
      </div>
      <div class="link-list">
        <p class="link-header">for organizations</p>
        <hr class="link-line" />
        <router-link class="underline-text small-link-text" to="/partner">partner</router-link>
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

.underline-text {
    position: relative;
    text-decoration: none;
    &:hover {
      text-decoration: none;
      color: $accent-light !important;
      &:before {
        visibility: visible;
       /* -webkit-transform: scaleX(1);
        transform: scaleX(1); */
      }
    }
    &:before {
      content: "";
      position: absolute;
      width: 100%;
      height: 2px;
      bottom: 0;
      left: 0;
      background-color: $accent-light;
      visibility: hidden;
      -webkit-transform: scaleX(0);
      transform: scaleX(0);
      -webkit-transition: all 0.3s ease-in-out 0s;
      transition: all 0.3s ease-in-out 0s;
    }
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

.nav-container {
  background-color: $main-dark;
  padding: 50px;
  width: 100vw;
  display: flex;
  justify-content: space-between;
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
}
.text-group{
  padding-left: 20em;
}

.cta-group{
}
</style>
