<template>
    <div>
        <p> we;re in custom form with special property: {{ content }}</p>
        <button class="btn btn-primary" @click="runMethod" ></button>
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
