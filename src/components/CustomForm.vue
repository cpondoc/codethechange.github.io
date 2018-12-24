<template>
    <div class="content">
        <div class="row">
            <div id="leftCol" class="col-4">
                <p> we;re in custom form with special property: {{ content }}</p>
            </div>
            <div id="rightCol" class="col-8">
                <button class="btn btn-accent" @click="runMethod" >Here's some text</button>
            </div>
        </div>
    </div>
</template>
<script>
export default {
  name: 'CustomForm',
  props: [ 'content' ],
  methods: {
    runMethod () {
      this.content = 'something else'
    }
  }
}
</script>
<style lang="scss">
@import '../theme.scss';
p {
    color: map-get($theme-colors, primary)
}

#leftCol {
    background-color: #3212aa
}

#rightCol {
    background-color: #ab24cc
}
</style>
