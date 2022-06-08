<template>
  <!-- <div class="d-flex justify-content-around">
    <router-link class="btn btn-primary" to="/products">Back</router-link>
  </div> -->
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      }
    },
  name: 'productDelete',
  methods: {
    async removeProduct(id) {
      if (confirm(`Are you sure to delete this product?`)) {
        await axios.put(`product_is_available/${id}/`)
          .then(response => {
            if (response.status === 200) {
                alert('Category deleted');
                this.$router.push('/products');
            }
          }).catch(error => {
              console.log(error)
          })
      }
    }
  },
  mounted() {
    this.removeProduct(this.$route.params.id);
  }
}
</script>