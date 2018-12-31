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
  text-align: center;
  color: #ffffff;
  background-color: #3b3b3b;
}

.nav-container {
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
