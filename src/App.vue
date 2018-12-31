<template>
  <div id="app">
    <div class="nav-container">
      <router-link id="logo" to="/">LOGO</router-link>
      <div id="links">
        <router-link class="link-text" to="/people">people</router-link>
        <router-link class="link-text" to="/projects">projects</router-link>
        <router-link class="link-text" to="/partner">partner</router-link>
        <router-link class="link-text" to="/join" id="join-link">join</router-link>
      </div>
    </div>
    <router-view/>
    <div id="footer">
      <div class="link-list">
        <p class="link-header">for students</p>
        <hr class="link-line" />
        <router-link class="small-link-text" to="/people">people</router-link>
        <br /> <br />
        <router-link class="small-link-text" to="/projects">projects</router-link>
        <br /> <br />
        <router-link class="small-link-text" to="/join" id="join-link">join</router-link>
        <br /> <br />
      </div>
      <div class="link-list">
        <p class="link-header">for organizations</p>
        <hr class="link-line" />
        <router-link class="small-link-text" to="/partner">partner</router-link>
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
  color: $accent-light !important;
}

#logo {
  margin-left: 100px;
}

.link-text {
  font-family: Comfortaa;
  font-size: 24px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff !important;
}

#links {
  margin-right: 80px;
  width: 570px;
  display: flex;
  justify-content: space-around
}

</style>
