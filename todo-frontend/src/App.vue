<script setup>
import Header from "@/components/Header.vue"
import inputField from "@/components/inputField.vue"
import displayTodos from "@/components/displayTodos.vue"
import {ref,onMounted} from 'vue';
import axios from "axios";

const todosIncompleted = ref([])
const todosCompleted= ref([])



  async function fetchData() {
  const res = await axios.get("http://127.0.0.1:5000/todos")
  const data =  await res.data
  todosIncompleted.value = data["incomplete_todos"]
  todosCompleted.value = data["completed_todos"]
}

fetchData()
 
 async function addTodo(inputValue) {
   await axios.post("http://127.0.0.1:5000/todos",{
       "todo" : inputValue

 })
 
 await fetchData()
}

 async function todoDone(id){
  await axios.post("http://127.0.0.1:5000/todos/complete", {

    'id':id
  })

  await fetchData()
}

async function todoDeleted(id){
  await axios.post("http://127.0.0.1:5000/todos/delete", {

    'id':id
  })
  await fetchData()

}

</script>

<template>
  <Header />
  <inputField @add-todo="addTodo"/>
  <displayTodos 
    :todosIncompleted= "todosIncompleted" 
    :todosCompleted="todosCompleted" 
    @todo-completed="todoDone"
    @delete-todo="todoDeleted" />
</template>

<style scoped>

</style>
