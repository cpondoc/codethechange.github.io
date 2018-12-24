<template>
    <custom-form :content="'happy times'" >
    </custom-form>
</template>
<script>
import CustomForm from '../components/CustomForm.vue'
export default {
  data: function () {
    return {
      myString: 'happy times'
    }
  },
  name: 'Partner',
  components: { CustomForm }
}
</script>
