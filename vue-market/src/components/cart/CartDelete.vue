<template lang="">
  <div>
    
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'cart-delete',
  methods: {
    async removeCart() {
      if (confirm('Are you sure want to remove cart?')) {
        console.log(this.$route.params.id);
        await axios.delete(`cart/${this.$route.params.id}/`)
          .then(response => {
            if (response.status === 204) {
              alert('Cart deleted');
              this.$router.push({ name: 'carts' });
            }
          }).catch(error => {
              console.log(error)
          })
      } else {
        this.$router.push({ name: 'carts' });
      }
    }
  },
  mounted() {
      this.removeCart();
    },
}
</script>
<style lang="">
  
</style>