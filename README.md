# Django_Restapi_Project (TODO List APP API) 
<div>
<p>TODO is an API for the platform where users to keep a track of the daily basis task and complete based on priority.
Users can create an account and create the TODO then add all the task that has to be completed based on their requirement and add the tasks based on the priority and set task completed </p>
<p>API is built uisng (Django, Django REST framework, django-rest-framework-simplejwt, serializers, ORM and sqlite3)</p>
</div>  
<h2>Buisness Logic</h2>
    <h3>Users Work Flow</h3>
    <ul>
        <li>User should register and login to it</li>
        <li>User should be able to create a new todo</li>
        <li>later the User can add the tasks in it(created todo)</li>
        <li>the task List will be sorted based</li>
        <ul>
          <li>First Priority Based on the priority index</li>
          <li>Second Priority Based on the Timestamp</li>  
        </ul>
        <li>There will be two list todo and done list</li>
        <li>User can also create multiple todo</li>       
    </ul>
<h2>API ENDPOINTS</h2>
        <div class="endpoints_div">
            <h3>Registration  (Post Method)</h3>
            <ul>
                <li>EndPoint: <span class="remoteURL">https://todolist-restapi.herokuapp.com/</span><span>api/accounts/auth/register/</span></li>
                <li><span>data that needed to be passed </span>
                    <pre>
                        {
                        "email": "tc2@gmail.com",
                        "username": "tc2", 
                        "password": "1234",
                        "password2": "1234"
                        }
                    </pre>    
                </li>
            </ul>
            <h3>Login (Post Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://todolist-restapi.herokuapp.com/</span><span>api/accounts/auth/</span></li>
                <li><span>data that needed to be passed </span>
                    <pre>
                                        {
                                        "username": "tc2@gmail.com",
                                        "password": "1234"
                                        }
                    </pre>
                </li>
            </ul>
            <h3>Adding header data to all the below-mentioned API calls</h3>
            <ul>
                <li>After Logging/Register we will be getting the access token as a response we need to add the access token as header to next API call</li>
                <li><span>Data that needed to be passed as a header</span>
                    <pre>
                        {
                            "Authorization": "Bearer "+ response_from_login['access']
                        }
                    </pre>    
                </li>
            </ul>
            <h3>Todo List creation and listing (Creation Post method and listing Get Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://todolist-restapi.herokuapp.com/</span><span>api/todolist/todoserializers/</span></li>
                <li><span>data that needed to be passed for todo creation </span>
                    <pre>
                                        {
                                            "todolistname": "TodoList_name"
                                        }
                    </pre>
                </li>
            </ul>    
            <h3>Task Create and Listing of the task in mentioned todolist (Creation Post method and listing Get Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://todolist-restapi.herokuapp.com/</span><span>api/todolist/tasklistserializers/</span></li>
                <li><span>Data that needed to be passed for Task Creation </span>
                    <pre>
                        {
                                "todolistid": 1,
                                "taskname": "task_Name",
                                "priority": 0
                        }
                    </pre>
                </li>
            </ul>    
            <h3>Task Delete and Update (Deletion Delete method and Update Put Method)</h3>
            <ul>
                <li>EndPoint:<span class="remoteURL">https://todolist-restapi.herokuapp.com/</span><span>api/todolist/taskserializers/</span></li>
                <li><span>Data that needed to be passed for Task Update for Task Delete only id is enough</span>
                    <pre>
                        {
                                    "todolistid": 1,
                                    "id": 18,
                                    "taskname": "task_Name",
                                    "priority": 0,
                                    "status":True
                        }
                    </pre>
                </li>
            </ul>
        </div>
