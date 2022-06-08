<template lang="">
  <div>
    
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'cart-add',
  methods: {
    async addCart() {
      if (confirm('Are you sure want to add new cart?')) {
        await axios.post('carts/')
          .then(response => {
            if (response.status === 201) {
              alert('Cart added');
              this.$router.push({ name: 'carts' });
            }
          }).catch(error => {
              console.log(error)
          })
      }
    }
  },
  mounted() {
      this.addCart();
    },
}
</script>
<style lang="">
  
</style>