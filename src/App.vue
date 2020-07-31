<template>
  <div id="app">
    <div :class="{ 'res': res }" id="nav-bar">
      <router-link id="logo" to="/" @click.native="toggleRes(false)">
        <img src="@/assets/img/wordmark.png"/>
      </router-link>
      <div id="links">
        <span class="nav-links">
          <router-link class="link-text nav-text color-change" to="/people" @click.native="toggleRes(false)">people</router-link>
          <router-link class="link-text nav-text color-change" to="/culture" @click.native="toggleRes(false)">culture</router-link>
          <router-link class="link-text nav-text color-change" to="/projects" @click.native="toggleRes(false)">projects</router-link>
          <router-link class="link-text nav-text color-change" to="/partner" @click.native="toggleRes(false)">partner</router-link>
          <router-link class="link-text color-change" to="/join" id="join-link" @click.native="toggleRes(false)">join</router-link>
        </span>
      </div>
      <a href="javascript:void(0);" id="res-icon" @click="toggleRes(!res)">
        <i class="fa fa-bars color-change"></i>
      </a>
    </div>
    <hr id="scroll-shadow" />
    <router-view id="page"/>
    <div id="footer">
      <div class="link-list">
        <p class="link-header">for students</p>
        <hr />
        <router-link class="small-link-text color-change" to="/people">people</router-link>
        <br /> <br />
        <router-link class="small-link-text color-change" to="/projects">projects</router-link>
        <br /> <br />
        <router-link class="small-link-text color-change" to="/join" id="join-small-link">join</router-link>
        <br /> <br />
      </div>
      <div class="link-list">
        <p class="link-header">for organizations</p>
        <hr />
        <router-link class="small-link-text color-change" to="/partner">partner</router-link>
        <br /> <br />
      </div>
    </div>
    <div id="info">
      <h6> Stanford Code the Change ©️2019 </h6>
    </div>
  </div>
</template>

<script>
import 'bootstrap'

export default {
  name: 'App',
  data () {
    return {
      res: false
    }
  },
  methods: {
    toggleRes (s) {
      this.res = s
    }
  }
}
</script>

<style lang="scss">
@import './theme.scss';

body {
  background-color: $main-dark;
  height: 100%;
}

.color-change {
  color: #ffffff;
  &:hover {
    text-decoration: inherit;
    color: $accent-light;
  }
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #ffffff;
  background-color: $main-dark;
  a {
    text-decoration: none;
    &.link-text {
      font-size: 18px;
      font-family: Comfortaa;
      font-weight: bold;
    }
    &.small-link-text {
      font-size: 20px;
      font-family: Comfortaa;
      font-weight: bold;
    }
  }
}

#nav-bar {
  position: sticky;
  top: -8px;
  z-index: 5;
  background-color: $main-dark;
  padding: 25px 60px;
  @media only screen and (max-width: 900px) {
    padding: 15px 20px;
  }
  display: flex;
  justify-content: flex-end;
  align-items: center;
  flex-wrap: wrap;
  #logo {
    margin-right: auto;
    img {
      max-height: 2.1em;
      @media only screen and (max-width: 900px) {
        max-height: 1.5em;
      }
    }
  }
  #links {
    .nav-text {
      padding-right: 3em;
    }
    #join-link {
      border: 2px solid white;
      border-radius: 8px;
      padding: 0.7em 1.3em;
      &:hover{
        border-color: $accent-light;
      }
    }
  }
  #res-icon {
    display: none;
  }
  @media only screen and (max-width: 900px) {
    .nav-links {
      display: none;
    }
    #res-icon {
      display: block;
      font-size: 1.4em;
    }
    &.res {
      #links {
        order: 3;
        flex-basis: 100%;
        display: block;
        .nav-links {
          display: block;
          > * {
            padding: .5em 0;
            display: block;
          }
          #join-link {
            border: none;
            padding: 0;
          }
        }
      }
    }
  }
}

/* Heavily inspired from https://stijndewitt.com/2018/06/12/pure-css-drop-shadow-on-scroll/ */
#scroll-shadow {
  width: 100%;
  height: 10px;
  position: sticky;
  top: 50px;
  z-index: 1000;
  box-shadow: 0 2px 19px 0 rgba(124, 124, 124, 0.5);
  z-index: 3;
  margin-top: -25px;
}

#footer {
  display: flex;
  flex-flow: row wrap;
  padding-left: 60px;
  @media only screen and (max-width: 700px) {
    padding-left: 20px;
  }
  padding-top: 10vh;
  padding-bottom: 10vh;
  .link-list {
    margin-right: 85px;
    .link-header {
      font-family: Comfortaa;
      font-size: 24px;
      font-weight: bold;
      text-align: center;
      color: white;
    }
  }
  hr {
    background-color:$accent-light;
    height: 2px;
  }
}

#info {
  background-color: $main-medium;
  margin-bottom: 0;
  padding: 30px;
  padding-left: 60px;
  @media only screen and (max-width: 700px) {
    padding-left: 20px;
  }
}
</style>
