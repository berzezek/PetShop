<template>
  <div class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
		<br class="mt-5">
    <category-add @create="addCategory"></category-add>
    <div class="container">
          
      <table class="table table-striped">
        <thead>
          <tr>
          <th scope="col">#</th>
          <th scope="col">Title</th>
          <th scope="col">Options</th>
          </tr>
        </thead>
        
        <tbody>
          
          <tr v-for='category in availableCategories' :key="category.id">
              
            <th scope="row">{{ category.id }}</th>
            <td>{{ category.name }}</td>
              <td>
                <div class="d-flex justify-content-evenly">
                  <router-link class="text-success" :to='{ name: "productAdd", params: { name: category.name, id: category.id } }'>
                    <i title="Add product" class="bi bi-file-plus"></i>
                  </router-link>
                  <router-link class="text-primary" :to='{ name: "categoryEdit", params: {name: category.name, description: category.description, id: category.id}}'>
                  <div title="Edit category">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil" viewBox="0 0 16 16">
                      <path d="M12.146.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1 0 .708l-10 10a.5.5 0 0 1-.168.11l-5 2a.5.5 0 0 1-.65-.65l2-5a.5.5 0 0 1 .11-.168l10-10zM11.207 2.5 13.5 4.793 14.793 3.5 12.5 1.207 11.207 2.5zm1.586 3L10.5 3.207 4 9.707V10h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.293l6.5-6.5zm-9.761 5.175-.106.106-1.528 3.821 3.821-1.528.106-.106A.5.5 0 0 1 5 12.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.468-.325z"/>
                    </svg>
                  </div>
                  </router-link>
                  <router-link class="text-danger" :to='{ name: "categoryDelete", params: {id: category.id}}'>
                  <div title="Remove category">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-file-x" viewBox="0 0 16 16">
                      <path d="M6.146 6.146a.5.5 0 0 1 .708 0L8 7.293l1.146-1.147a.5.5 0 1 1 .708.708L8.707 8l1.147 1.146a.5.5 0 0 1-.708.708L8 8.707 6.854 9.854a.5.5 0 0 1-.708-.708L7.293 8 6.146 6.854a.5.5 0 0 1 0-.708z"/>
                      <path d="M4 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H4zm0 1h8a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/>
                    </svg>
                  </div>
                  </router-link>
                  <router-link class="text-info" :to='{ name: "categoryDetail", params: { name: category.name, description: category.description, id: category.id }}'>
                    <div title="Category details">
                      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-three-dots-vertical" viewBox="0 0 16 16">
                        <path d="M9.5 13a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0zm0-5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0z"/>
                      </svg>
                    </div>
                  </router-link>
                </div>
                
            </td>
          </tr>
          
        </tbody>
        
      </table>
      

    </div>

  </div>

</template>

<script>
import axios from 'axios';
import CategoryAdd from '@/components/category/CategoryAdd.vue';

export default {
  components: {
    CategoryAdd
  },
  data() {
    return {
      categories: [],
      availableCategories: [],
      name: '',
      description: ''
    }
  },
  methods: {
    async getCategory() {
      await axios.get('categories/')
        .then(response => {
          this.categories = response.data;
          this.filterByAvailable();
        })
        .catch(error => {
          console.log(error)
        })
    },
    async addCategory(category) {
      await axios.post('categories/', {
        name: category.name,
        description: category.description
      }).then(response => {
        if (response.status === 201) {
          this.getCategory();  
          alert('Category added');  
        }
      }).catch(error => {
        console.log(error)
      })
    },
    addProduct(id) {
      console.log(id)
    },
    filterByAvailable() {
			this.categories.forEach(category => {
				if (category.is_available === true) {
					this.availableCategories.push(category);
				}
			})
		},
  },
  mounted() {
    this.getCategory()
  },
  filters: {
      // capitalize: function (value) {
      //     if (!value) return ''
      //     value = value.toString()
      //     return value.charAt(0).toUpperCase() + value.slice(1)
      // }
  }

}
</script>

<style scoped>

</style>