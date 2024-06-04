<script setup>
    import {inject} from 'vue'
    import Card from './Card.vue'

    defineProps({
        items: Array
    })

    const onClickAdd = () => {
        alert('111')
    }

    const addToFavorite = inject('addToFavorite')

</script>


<template>
    <div class="grid grid-cols-4 gap-5">
        <Card
            v-for="item in items"
            :key="item.id"
            :price="item.price" 
            :imageUrl="item.image" 
            :title="item.title"
            :onClickAdd="onClickAdd"
            :isFavorite="item.isFavorite"
            :onClickFavorite="() => addToFavorite(item)"
            :id="item.id"
        />    
    </div>    
</template>