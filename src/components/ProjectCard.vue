<template>
    <div class="col-sm card case-card">
        <div class="case-card-text">
          <h6>TEACH FOR AMERICA</h6>
          <p>How we built a scalable donor matching plaform.</p>
        </div>
        <img
          alt="social good image"
          src="http://unbounce.com/photos/landing-pages-that-could-be-marketing-more-money.png">
        <h6 class="link-case"><a href="#" id="link-1">READ CASE</a></h6>
      </div>
</template>

<script>

export default {
  name: 'ProjectCard',
  props: [],
  data: function () {
  }
}
</script>

<style scoped lang="scss">

.card {
  margin: 2em;
  padding: 1em 0;
  .case-card-text {
    margin: 0.7em;
  }
  img {
    width: 100%;
    height: auto;
    margin: 0.5em auto 1em;
  }
}

.case-card {
  background-color: #292929;
  .link-case {
    text-align: right;
    margin: 0.7em;
    #link-1 {
      color: #fff469;
    }
    #link-2 {
      color: rgb(233, 97, 233);
    }
    #link-3 {
      color: rgb(167, 255, 255);
    }
    a {
      text-decoration: none;
      &:hover {
        text-decoration: none;
        color: inherit;
      }
    }
  }
}

.project-card {
  color: #000000;
  border: none;
}

</style>
