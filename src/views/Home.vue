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
        <img id="stanford" src="@/assets/img/stanford@2x.png" />
      </div>
    </div>
    <div class="row">
      <div class="col-12">

      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'home',
  components: {

  }
}
</script>

<style scoped lang="scss">
@import '../theme.scss';
.container {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  padding: 0px;
}

.row {
  margin:0px;
  width: 100vw;
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
