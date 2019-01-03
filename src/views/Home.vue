<template>
  <div>
    <div class="row">
      <div class="container">
        <div id="text">
          <br />
          <h1 id="hook">Code from day one, with impact.</h1>
          <hr id="line" />
          <p id="subtitle">Welcome to a passionate club of engineers and makers.</p>
          <br />
          <br />
          <router-link id="view-text" to="/projects">View our work</router-link>
          <br />
        </div>
        <img v-if="width > 1000" id="stanford" src="@/assets/img/stanford@2x.png" />
      </div>
    </div>
    <div class="row">
      <div class="center-horiz col-5 col-xs-12">
        <div class="text-content">
          <div class="center-space">
            <p class="year">2018</p>
            <p class="org-name">Teach For America</p>
            <p class="subtitle">We built a project matching platform that boosted engagement by 60%.</p>
            <br />
            <button @click="TODO()" class="btn read-btn">READ</button>
          </div>
        </div>
      </div>
      <div class="col-7 col-xs-12 image-holder">
        <img class="image" src="@/assets/img/sketch@2x.png"/>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  data () {
    return {
      width: 0,
      height: 0
    }
  },
  mounted () {
    window.addEventListener('resize', this.handleResize)
    this.handleResize()
  },
  destroyed () {
    window.removeEventListener('resize', this.handleResize)
  },
  methods: {
    handleResize () {
      this.width = window.innerWidth
      this.height = window.innerHeight
    }
  },
  components: {

  }
}
</script>

<style scoped lang="scss">
@import '../theme.scss';

.image {
  height: 100%;
}

.image-holder:before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0,255,255, 0.5);
  transition: all .3s linear;
}

.read-btn {
  width: 281px;
  height: 95px;
  border-radius: 100px;
  box-shadow: 0 2px 10px 0 rgba(151, 33, 255, 0.5);
  background-color: $bold-purple;
  font-family: 'Open Sans';
  font-size: 24px;
  font-weight: 800;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  color: #ffffff;
}

.subtitle {
  font-family: Comfortaa;
  font-size: 25px;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.5;
  letter-spacing: normal;
  color: #ffffff;
}

.text-content {
  width: 400px;
  height: 100%;
}

.center-horiz {
  display: flex;
  justify-content: center;
}

.center-space {
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 100%;
}

.org-name {
  font-family: Comfortaa;
  font-size: 48px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  color: #ffffff;
}

.year {
  font-family: Comfortaa;
  font-size: 32px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  color: #d5a5ff;
}

.container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 0px;
}

.row {
  margin:0px;
  height: calc(100vh - 75px);
}

#text {
  width: 500px;
}

#line {
  width: 125px;
  height: 2px;
  background-color: $home-accent;
  margin-left: 0px;
}

#subtitle {
  font-family: Comfortaa;
  font-size: 30px;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  color: #ffffff;
}

#hook {
  font-family: Comfortaa;
  font-size: 60px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  color: #ffffff;
}

#view-text {
  font-family: Comfortaa;
  font-size: 32px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: normal;
  letter-spacing: normal;
  color: $home-accent;
}

#stanford {
  width: 30em;
  height: 30em;
}
</style>
