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
          <a href="#" v-scroll-to="'.text-content'" @click="scrollToProjects" id="view-text">View our work</a>
          <br />
          <br />
        </div>
        <img id="stanford" src="@/assets/img/stanford@2x.png" />
      </div>
    </div>
    <div v-for="project in caseStudies" :key="project.name" class="row">
      <div class="center-horiz col-lg-5 col-sm-12">
        <div class="text-content">
          <div class="center-space">
            <p class="year" :style="{ color: themeColors['light-'+project.color] }">{{ project.year }}</p>
            <p class="org-name">{{ project.name}}</p>
            <p class="subtitle">{{ project.subtitle }}</p>
            <br />
            <button @click="TODO()" :style="{ backgroundColor: themeColors['bold-'+project.color] }" class="btn read-btn">READ</button>
             <br />
            <br />
          </div>
        </div>
      </div>
      <div  :style="{ background: themeColors['tint-'+project.color] }" class="col-lg-7 col-sm-12 image-holder">
        <img class="image" :src="baseUrl + project.background" />
      </div>
    </div>
  </div>
</template>

<script>
import Projects from '@/data/projects.json'

export default {
  name: 'home',
  data () {
    const colors = ['blue', 'yellow', 'purple']
    let i = 0
    let caseStudies = []
    for (let x of Projects) {
      if (x.featured) {
        x.color = colors[i++ % colors.length]
        caseStudies.push(x)
      }
    }
    return {
      caseStudies: caseStudies,
      width: 0,
      height: 0,
      baseUrl: process.env.BASE_URL,
      themeColors: {
        'light-purple': '#d5a5ff',
        'light-yellow': 'fff469',
        'light-blue': '#5ea9ff',
        'tint-purple': 'rgba(213, 165, 255, 0.3)',
        'tint-yellow': 'rgba(255, 244, 105, 0.3)',
        'tint-blue': 'rgba(94, 169, 255, 0.3)',
        'bold-blue': '#3190ff',
        'bold-purple': '#9721ff',
        'bold-orange': '#ff9d14',
        'bold-yellow': '#fff469'
      }

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
    },
    scrollToProjects () {

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
  width: 100%;
}

.image-holder:before {
  content: "";
  display: block;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
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
}

.container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 0px;
}

.row {
  margin:0px;
  min-height: calc(100vh - 75px);
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
