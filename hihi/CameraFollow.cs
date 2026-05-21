using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    private float x, y;
    [SerializeField] private GameObject player;
    void Start()
    {
        gameObject.transform.position = new Vector3(player.transform.position.x, player.transform.position.y, -10);
    }

    void Update()
    {
        Follow();
    }

    

    private void Follow()
    {
        gameObject.transform.position = new Vector3(player.transform.position.x, player.transform.position.y, -10);
    }
}
