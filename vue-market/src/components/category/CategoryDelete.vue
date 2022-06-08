<template>
  <div class="d-flex justify-content-around">
    <h1 class="title">Category deleted</h1>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      }
    },
  name: 'remove-category',
  methods: {
    async removeCategory(id) {
      if (confirm(`Are you sure to delete this category?`)) {
        await axios.put(`category_is_available/${id}/`)
          .then(response => {
            console.log(response);
            if (response.status === 200) {
                alert('Category deleted');
                this.$router.push('/categories');
            }
          }).catch(error => {
              console.log(error)
          })

      } else {
        alert('Category not deleted');
        this.$router.push('/categories');
      }
    }
  },
  mounted() {
    this.removeCategory(this.$route.params.id);
  }
}
</script>